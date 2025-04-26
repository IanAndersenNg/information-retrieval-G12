package org.example;

import com.fasterxml.jackson.core.JsonFactory;
import com.fasterxml.jackson.core.JsonParser;
import com.fasterxml.jackson.core.JsonToken;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.apache.lucene.analysis.Analyzer;
import org.apache.lucene.analysis.CharArraySet;
import org.apache.lucene.analysis.en.EnglishAnalyzer;
import org.apache.lucene.analysis.standard.StandardAnalyzer;
import org.apache.lucene.document.*;
import org.apache.lucene.index.IndexOptions;
import org.apache.lucene.index.IndexWriter;
import org.apache.lucene.index.IndexWriterConfig;
import org.apache.lucene.store.Directory;
import org.apache.lucene.store.FSDirectory;

import java.io.File;
import java.io.IOException;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

public class YelpReviewSearchEngine {

    public static void indexReviews(String jsonPath, String indexDir) throws IOException {
        // combine Lucene English set with domain terms
        CharArraySet stopWords = CharArraySet.copy(EnglishAnalyzer.getDefaultStopSet());
        stopWords.addAll(List.of("yelp", "restaurant"));
        CharArraySet CUSTOM_STOP_WORDS = CharArraySet.unmodifiableSet(stopWords);

        Directory dir = FSDirectory.open(Paths.get(indexDir));
        Analyzer analyzer = new StandardAnalyzer(CUSTOM_STOP_WORDS);

        IndexWriterConfig cfg = new IndexWriterConfig(analyzer)
                .setOpenMode(IndexWriterConfig.OpenMode.CREATE);

        // Define a FieldType that stores positions, frequencies, offsets, and term vectors
        FieldType textFieldType = new FieldType();
        textFieldType.setTokenized(true);   // tokenize the text
        textFieldType.setStored(false);     // we don't need to store full text here
        textFieldType.setIndexOptions(IndexOptions.DOCS_AND_FREQS_AND_POSITIONS_AND_OFFSETS);
        // inverted index with positions & offsets :contentReference[oaicite:3]{index=3}
        textFieldType.setStoreTermVectors(true);
        textFieldType.setStoreTermVectorPositions(true);
        textFieldType.setStoreTermVectorOffsets(true);
        // term vectors also include positions & offsets :contentReference[oaicite:4]{index=4}
        textFieldType.freeze();
        try (IndexWriter writer = new IndexWriter(dir, cfg);
             JsonParser parser = new JsonFactory().createParser(new File(jsonPath))) {
            ObjectMapper mapper = new ObjectMapper();
            List<Long> times = new ArrayList<>();
            long startAll = System.nanoTime();
            // Each review in the dataset is separated by a new line
            // The following number is retrieved by running wc -l yelp_academic_dataset_review.json
            long totalDocs = 6990280;
            System.out.println("Total documents to index: " + totalDocs);
            long count = 0, nextCheckpoint = totalDocs / 10;
            System.out.println("Index process started...");
            while (parser.nextToken() != null) {
                if (parser.currentToken() == JsonToken.START_OBJECT) {
                    Review r = mapper.readValue(parser, Review.class);

                    Document doc = new Document();
                    doc.add(new StringField("review_id", r.review_id, Field.Store.YES));
                    doc.add(new StringField("user_id", r.user_id, Field.Store.YES));
                    doc.add(new StringField("business_id", r.business_id, Field.Store.YES));
                    doc.add(new IntPoint("stars", r.stars));
                    doc.add(new StoredField("stars", r.stars));
                    doc.add(new LongPoint("date", r.date.getTime()));
                    doc.add(new StoredField("date", r.date.getTime()));
                    doc.add(new IntPoint("useful", r.useful));
                    doc.add(new StoredField("useful", r.useful));
                    doc.add(new IntPoint("funny", r.funny));
                    doc.add(new StoredField("funny", r.funny));
                    doc.add(new IntPoint("cool", r.cool));
                    doc.add(new StoredField("cool", r.cool));
                    // Use custom textFieldType for the review text
                    doc.add(new Field("text", r.text, textFieldType));
                    writer.addDocument(doc);

                    count++;
                    if (count == nextCheckpoint) {
                        long t = System.nanoTime() - startAll;
                        times.add(t);
                        double pct = nextCheckpoint / totalDocs;
                        nextCheckpoint += totalDocs / 10;
                        System.out.printf("Indexed %,d/%,d (%.1f%%)%n", count, totalDocs, pct);
                    }
                }
            }
            writer.commit();
            long totalTime = System.nanoTime() - startAll;
            System.out.println("Process completed in " + totalTime);
        }
    }

}
