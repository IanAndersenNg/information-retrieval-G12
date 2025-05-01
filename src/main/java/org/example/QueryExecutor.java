package org.example;

import java.io.IOException;
import java.nio.file.Paths;

import org.apache.lucene.document.Document;
import org.apache.lucene.index.DirectoryReader;
import org.apache.lucene.index.Term;
import org.apache.lucene.search.IndexSearcher;
import org.apache.lucene.search.ScoreDoc;
import org.apache.lucene.search.TermQuery;
import org.apache.lucene.search.TopDocs;
import org.apache.lucene.store.FSDirectory;

public class QueryExecutor implements AutoCloseable {
    private final IndexSearcher searcher;

    public QueryExecutor(String indexDir) throws IOException {
        var reader = DirectoryReader.open(FSDirectory.open(Paths.get(indexDir)));
        this.searcher = new IndexSearcher(reader);
    }

    /** Runs a TermQuery on `field` for the exact `termText` and prints top‐N hits. */
    public void termQuery(String field, String termText, int topN) throws IOException {
        var query = new TermQuery(new Term(field, termText));
        TopDocs results = searcher.search(query, topN);        

        System.out.printf("Found %d hits for %s:%s%n", results.totalHits.value, field, termText);
        for (ScoreDoc sd : results.scoreDocs) {
            Document doc = searcher.doc(sd.doc);
            String reviewId = doc.get("review_id");
            String text     = doc.get("text");
            String stars    = doc.get("stars");

            System.out.printf(
              "docID=%d | score=%.3f | review_id=%s | review=%s | stars=%s%n",
              sd.doc, sd.score, reviewId, text, stars
            );
        }
    }

    public void close() throws IOException {
        searcher.getIndexReader().close();
    }
}