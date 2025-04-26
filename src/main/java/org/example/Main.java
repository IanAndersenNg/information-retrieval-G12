package org.example;

import java.io.IOException;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        //TIP Press <shortcut actionId="ShowIntentionActions"/> with your caret at the highlighted text
        // to see how IntelliJ IDEA suggests fixing it.
        System.out.println("Hello and welcome!");

        if (args.length < 1) {
            System.err.println("Usage: java YelpReviewSearchEngine index <jsonPath> <indexDir>");
            System.err.println("   or: java YelpReviewSearchEngine search <indexDir> <query> <topN>");
            System.exit(1);
        }
        switch (args[0]) {
            case "index" -> {
                try {
                    YelpReviewSearchEngine.indexReviews(args[1], args[2]);
                } catch (IOException e) {
                    System.err.println(e.getMessage());
                    throw new RuntimeException(e);
                }
            }
            case "search" -> {
                // implement search here
            }
            default -> System.err.println("Unknown command: " + args[0]);
        }

    }
}