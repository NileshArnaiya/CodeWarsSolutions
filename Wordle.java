import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Objects;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Wordle {

    public static int getLevenshteinDistance(String X, String Y)
    {
        int m = X.length();
        int n = Y.length();

        int[][] T = new int[m + 1][n + 1];
        for (int i = 1; i <= m; i++) {
            T[i][0] = i;
        }
        for (int j = 1; j <= n; j++) {
            T[0][j] = j;
        }

        int cost;
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                cost = X.charAt(i - 1) == Y.charAt(j - 1) ? 0: 1;
                T[i][j] = Integer.min(Integer.min(T[i - 1][j] + 1, T[i][j - 1] + 1),
                        T[i - 1][j - 1] + cost);
            }
        }

        return T[m][n];
    }

    public static double findSimilarity(String x, String y) {
        if (x == null || y == null) {
            throw new IllegalArgumentException("Strings must not be null");
        }

        double maxLength = Double.max(x.length(), y.length());
        if (maxLength > 0) {
            // optionally ignore case if needed
            return (maxLength - getLevenshteinDistance(x, y)) / maxLength;
        }
        return 1.0;
    }

    public static void main(String[] args) throws IOException {

        File file = new File(
                "C:\\Users\\nILESH JAIN\\Desktop\\w11-prep\\Poker2\\src\\words.txt");

        BufferedReader br
                = new BufferedReader(new FileReader(file));

        String st;
        ArrayList<String> fiveLetterWords = new ArrayList<>();
        while ((st = br.readLine()) != null) {

            if (st.length() == 5) {
                fiveLetterWords.add(st);
            }
        }
        for(int i = 0; i< fiveLetterWords.size(); i++){
            System.out.println(fiveLetterWords.get(i));
        }
        Collections.shuffle(fiveLetterWords);
        String secretWord = fiveLetterWords.get(0);

        Scanner sc = new Scanner(System.in);
        System.out.println("");
        System.out.println("-^Possible Words^-");

        while(true) {
            int count = 0;
            System.out.println("\nTake a guess at the word :- ");
            String userGuessed = sc.nextLine();
            if(userGuessed.equals(secretWord)){
                System.out.println("You guessed it right! ");
                break;
            }


            if(userGuessed.length() != 5)
            {
                System.out.println("Word is not on the list! Try Again");
                continue;
            }
            else if(userGuessed.length()==5) {
                for (int i = 0; i < fiveLetterWords.size(); i++) {
                    double similarity = findSimilarity(fiveLetterWords.get(i), userGuessed);
                    if (similarity > 0.78 && count < 3) {
                        System.out.println("This are the possible words " + fiveLetterWords.get(i));
                        count +=1;
                    }
                }
                for (int i = 0; i < userGuessed.length(); i++) {
                    if (userGuessed.charAt(i) == secretWord.charAt(i)) {
                        System.out.print("1");
                    } else if (secretWord.contains("" + userGuessed.charAt(i)) && !(userGuessed.charAt(i) == secretWord.charAt(i))) {
                        System.out.print("2");
                    } else {
                        System.out.print("0");
                    }
                }
            }

            //System.out.println("\n1 means correct letter and position; 2 means correct letter wrong position; 0 means miss");
        }
    }
}