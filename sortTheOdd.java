import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class Kata {
  public static int[] sortArray(int[] array) {
    // loop through all odd numbers
        // add to seperate lists of odds and their indices
        // sort the odds list
        // convert to int[] array and substitute indice values with values.
        // should've used hashmap here.

        List<Integer> listOfIndices = new ArrayList<>();
        List<Integer> listOfOdds = new ArrayList<>();
        for(int i =0; i < array.length; i++){
            if(array[i] % 2 != 0){
                listOfIndices.add(i);
                listOfOdds.add(array[i]);
            }
        }
        // sort the list of odds
        Collections.sort(listOfOdds);

        int[] arrOdds = listOfOdds.stream().mapToInt(i -> i).toArray();
        int[] arrIndices = listOfIndices.stream().mapToInt(i -> i).toArray();

        for(int i = 0; i < arrIndices.length; i++){
            array[arrIndices[i]] = arrOdds[i];
        }

        return array;
  }
}