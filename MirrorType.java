// Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

// Examples: spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" spinWords( "This is a test") => returns "This is a test" spinWords( "This is another test" )=> returns "This is rehtona test"

public class MirrorType {

  public String spinWords(String sentence) {
    //TODO: Code stuff here
    // split based on spaces 
        String arr[] = sentence.split(" ");
        StringBuilder sbf = new StringBuilder();
        for(int i = 0; i < arr.length; i++){
            // iterate through string elements and check length > 5 
            if(arr[i].length() >= 5){
              // replace the current one with reverse using StringBuilder
                arr[i] = arr[i].replace(arr[i], new StringBuilder(arr[i]).reverse().toString());
            }
            sbf.append(arr[i] + " ");
        }
//        System.out.print(Arrays.toString(arr));
        return sbf.toString().trim();
    
  }
}