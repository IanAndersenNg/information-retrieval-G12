package org.example;

import java.io.IOException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        System.out.println("Hello welcome to Yelp Review Search Engine !!");

        while (true) {
            System.out.println("1=index  2=search  3=exit");
            String o = sc.nextLine().trim();
            if ("1".equals(o)) {
                System.out.print("jsonPath: ");
                String j = sc.nextLine().trim();
                System.out.print("indexDir: ");
                String idx = sc.nextLine().trim();
                YelpReviewSearchIndexer.indexReviews(j, idx);

            } else if ("2".equals(o)) {
                System.out.print("indexDir: ");
                String idx = sc.nextLine().trim();
                System.out.print("field: ");
                String f = sc.nextLine().trim();
                System.out.print("term: ");
                String t = sc.nextLine().trim();
                System.out.print("topN: ");
                int n = Integer.parseInt(sc.nextLine().trim());
                try (QueryExecutor qe = new QueryExecutor(idx)) {
                    qe.termQuery(f, t, n);
                }

            } else if ("3".equals(o)) {
                break;
            }
        }
        sc.close();
    }
}