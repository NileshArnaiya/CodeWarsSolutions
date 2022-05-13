//For statues = [6, 2, 3, 8], the output should be
//        solution(statues) = 3.
//
//        Ratiorg needs statues of sizes 4, 5 and 7.

import java.util.Arrays;

public class findMissingStatue {


    public static boolean contains(final int[] arr, final int key) {
        return Arrays.stream(arr).anyMatch(i -> i == key);
    }

    int solution(int[] statues) {

        Arrays.sort(statues);
        int count = 0;
        for(int i = statues[0]; i < statues[statues.length-1]; i++){

            System.out.println("String is " + i);
            if(!contains(statues, i)){
                count++;
            }
        }
        return count;
    }

}
