import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class TryOut {


    static boolean solution(int[] sequence) {

        boolean strict = false;
        int[] integers = new int[sequence.length];
        for(int i = 0; i < sequence.length - 1; i++){
            if(sequence[i] < sequence[i+1]){
                System.out.println("Strictly increasing");
                strict = true;
            }
            else{
                integers
                strict = false;

            }
        }

        return strict;
    }


    public static void main(String[] args) {


        solution(new int[] { 1, 3, 2, 1});

    }



}
