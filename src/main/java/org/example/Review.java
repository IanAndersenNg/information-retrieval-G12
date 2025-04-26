package org.example;


import com.fasterxml.jackson.annotation.JsonFormat;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class Review {

    public String  review_id;
    public String  user_id;
    public String  business_id;
    public int     stars;
    @JsonFormat(shape = JsonFormat.Shape.STRING, pattern = "yyyy-MM-dd HH:mm:ss")
    public java.util.Date date;
    public int     useful;
    public int     funny;
    public int     cool;
    public String  text;
    // Jackson requires a default constructor
    public Review() {}

}
