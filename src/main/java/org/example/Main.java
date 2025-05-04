package org.example;

import java.io.IOException;
import java.util.Scanner;

public class Main {

    private static final String INDEX_LOCATION = "search_index";

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        System.out.println("Hello welcome to Yelp Review Search Engine !!");

        while (true) {
            System.out.println("""
                Please select your operation:
                
                0 - Exit
                1 - Index documents
                2 - Search documents by term
                3 - Search documents by phrase
                4 - Get review by review_id
                """);
            String o = sc.nextLine().trim();
            if ("1".equals(o)) {
                System.out.print("jsonPath: ");
                String j = sc.nextLine().trim();
                YelpReviewSearchIndexer.indexReviews(j, INDEX_LOCATION);

            } else if ("2".equals(o)) {
                System.out.print("field: ");
                String f = sc.nextLine().trim();
                System.out.print("term: ");
                String t = sc.nextLine().trim();
                System.out.print("topN: ");
                int n = Integer.parseInt(sc.nextLine().trim());
                try (QueryExecutor qe = new QueryExecutor(INDEX_LOCATION)) {
                    qe.termQuery(f, t, n);
                }
            } else if ("3".equals(o)) {
                System.out.print("field: ");
                String f = sc.nextLine().trim();
                System.out.print("phrase: ");
                String t = sc.nextLine().trim();
                System.out.print("topN: ");
                int n = Integer.parseInt(sc.nextLine().trim());
                try (QueryExecutor qe = new QueryExecutor(INDEX_LOCATION)) {
                    qe.phraseQuery(f, t, n);
                }
            } else if ("4".equals(o)) {
                System.out.print("review_id: ");
                String reviewId = sc.nextLine().trim();
                try (QueryExecutor qe = new QueryExecutor(INDEX_LOCATION)) {
                    qe.retrieveReview(reviewId);
                }
            } else {
                break;
            }
        }
        sc.close();
    }
}