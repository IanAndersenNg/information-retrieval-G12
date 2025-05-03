package org.example;

import java.io.IOException;
import java.io.StringReader;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.regex.Pattern;

import org.apache.lucene.analysis.CharFilter;
import org.apache.lucene.analysis.TokenStream;
import org.apache.lucene.analysis.pattern.PatternReplaceCharFilter;
import org.apache.lucene.analysis.standard.StandardAnalyzer;
import org.apache.lucene.analysis.tokenattributes.CharTermAttribute;
import org.apache.lucene.document.Document;
import org.apache.lucene.index.DirectoryReader;
import org.apache.lucene.index.Term;
import org.apache.lucene.queryparser.flexible.standard.nodes.intervalfn.Phrase;
import org.apache.lucene.search.*;
import org.apache.lucene.store.FSDirectory;

public class QueryExecutor implements AutoCloseable {
    private final IndexSearcher searcher;

    public QueryExecutor(String indexDir) throws IOException {
        var reader = DirectoryReader.open(FSDirectory.open(Paths.get(indexDir)));
        this.searcher = new IndexSearcher(reader);
    }

    public void retrieveReview(String reviewId) throws IOException {
        var field = "review_id";
        var query = new TermQuery(new Term(field, reviewId));
        runQueryGetFullReview(query, String.format("Term Query(%s:%s)", field, reviewId), 1);
    }

    /** Runs a TermQuery on `field` for the exact `termText` and prints top‐N hits. */
    public void termQuery(String field, String termText, int topN) throws IOException {
        var query = new TermQuery(new Term(field, termText));
        runQuery(query, String.format("Term Query(%s:%s)", field, termText), topN);
    }

    /** Runs a PhraseQuery on `field` for `phraseText` and prints top‐N hits. */
    public void phraseQuery(String field, String phraseText, int topN) throws IOException {
        List<String> terms = normalizePhrase(phraseText);
        PhraseQuery.Builder builder = new PhraseQuery.Builder();
        builder.setSlop(0);  // exact phrase
        for (String term : terms) {
            builder.add(new Term(field, term));
        }
        var pq = builder.build();
        runQuery(pq, String.format("Phrase Query(%s)", phraseText), topN);
    }

    /**
     * Runs any Query and prints top‐N hits. Returns truncated review
     */
    private void runQuery(Query query, String description, int topN) throws IOException {
        TopDocs results = searcher.search(query, topN);
        System.out.printf("Found %d hits for %s%n", results.totalHits.value, description);
        for (ScoreDoc sd : results.scoreDocs) {
            Document doc = searcher.doc(sd.doc);
            System.out.printf(
                    "docID=%d | score=%.3f | review_id=%s | stars=%s | snippet=%s%n",
                    sd.doc,
                    sd.score,
                    doc.get("review_id"),
                    doc.get("stars"),
                    doc.get("text").replaceAll("(?s)(.{100}).*", "$1...")
            );
        }
    }

    /**
     * Returns full review text instead of truncated review
     */
    private void runQueryGetFullReview(Query query, String description, int topN) throws IOException {
        TopDocs results = searcher.search(query, topN);
        System.out.printf("Found %d hits for %s%n", results.totalHits.value, description);
        for (ScoreDoc sd : results.scoreDocs) {
            Document doc = searcher.doc(sd.doc);
            System.out.printf(
                    "docID=%d | score=%.3f | review_id=%s | stars=%s | snippet=%s%n",
                    sd.doc,
                    sd.score,
                    doc.get("review_id"),
                    doc.get("stars"),
                    doc.get("text")
            );
        }
    }

    /**
     * Strips punctuation from phrase, since indexer uses StandardAnalyzer which does not store punctuation with token
     */
    private List<String> normalizePhrase(String text) throws IOException {
        // 1. CharFilter: remove all non‑letter/digit (i.e. punctuation)
        CharFilter filter = new PatternReplaceCharFilter(
                Pattern.compile("[^\\p{L}\\p{Nd}]+"), " ",
                new StringReader(text));
        // 2. Tokenize & lower‑case with StandardAnalyzer
        List<String> tokens = new ArrayList<>();
        try (TokenStream ts = new StandardAnalyzer().tokenStream("text", filter)) {
            ts.reset();
            while (ts.incrementToken()) {
                tokens.add(ts.getAttribute(CharTermAttribute.class).toString());
            }
            ts.end();
        }
        return tokens;
    }

    public void close() throws IOException {
        searcher.getIndexReader().close();
    }
}