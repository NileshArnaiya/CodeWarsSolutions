import java.util.*;
public class DirectionsReduction {
    public static String[] dirReduc(String[] arr) {
        // Your code here.
        //        ArrayList<String> list = new ArrayList<>();

        List<String> list = new ArrayList<String>();
        for(String str : arr){
            list.add(str);
        }
        while (true) {
            int len = list.size();
            for (int i = 0; i < list.size() - 1; i++) {
                if ("NORTH".equals(list.get(i)) && "SOUTH".equals(list.get(i + 1)) ||
                        "SOUTH".equals(list.get(i)) && "NORTH".equals(list.get(i + 1)) ||
                        "EAST".equals(list.get(i)) && "WEST".equals(list.get(i + 1)) ||
                        "WEST".equals(list.get(i)) && "EAST".equals(list.get(i + 1))) {

                  // here index changes after one remove so you don't need to do remove on i+1 instead just use remove again. 
                    list.remove(i);
                    list.remove(i);
                    break;

                }
            }
           if( len == list.size()){
                break;
            }
            
        }
        return list.toArray(new String[list.size()]);
    }
}