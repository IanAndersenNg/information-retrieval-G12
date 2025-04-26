package org.example;


import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class Review {

    public String  review_id;
    public String  user_id;
    public String  business_id;
    public int     stars;
    public java.util.Date date;
    public int     useful;
    public int     funny;
    public int     cool;
    public String  text;
    // Jackson requires a default constructor
    public Review() {}

}
