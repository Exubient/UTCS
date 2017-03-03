/**
 */

import java.io.IOException;
import java.io.FileReader;
import java.io.BufferedReader;

import java.util.HashMap;
import java.util.LinkedList;
import javafx.util.Pair;
import java.util.List;
import java.util.Map;
// import java.util.regex.Matcher;
// import java.util.regex.Pattern;

public class Graph {
    private String _unlocked;
    private  Map<String,List<String>> Adjacency_List = new HashMap<String, List<String>>(); 
    /*
     * Creates a graph to represent the neighborhood, where unlocked is the file name for the unlocked houses
     * and keys is the file name for which houses have which keys.
     */

    public Graph(String unlocked, String keys) {
        read(unlocked);
        read(keys);

    }

    public void read(String filename){

        BufferedReader br = null;
        FileReader fr = null;
        String sCurrentLine;


        try {
            fr = new FileReader(filename);
            br = new BufferedReader(fr);
            br = new BufferedReader(new FileReader(filename));
            
            if (filename == "unlocked.txt"){
                while ((sCurrentLine = br.readLine()) != null) {
                    _unlocked = sCurrentLine;
                }
            }

            else { 
                while ((sCurrentLine = br.readLine()) != null) {

                    String[] parts = sCurrentLine.split(":");
                    System.out.println("you have added ___" + parts[0] + "____to the list");
                    Adjacency_List.put(parts[0], new LinkedList<String>());

                    if (parts.length > 1) {
                        //이거는 통으로 출력
                        System.out.println("you have added <LinkedList> ___" + parts[1] + "____to the edges");
                        // 여기다 저장 어떻게하냐->>>Adjacency_List.put(parts[0], new LinkedList<String>());


                        //이거는 하나 하나씩 출력
                        // String[] edges = sCurrentLine.split(",");
                        // for(String word:parts[1].substring(1).split(", ")){  
                        //     System.out.println("you have added _____" + word + "_____ to the edge"); 
                        // }
                    }
            }
        }

        } catch (IOException e) {
            e.printStackTrace();

        } finally {
            try {
                if (br != null)
                    br.close();
                if (fr != null)
                    fr.close();
            } catch (IOException ex) {
                ex.printStackTrace();
            }
        }
    }


    // public void setEdge(String source, String destination)
    // {
    //     if (source > Adjacency_List.size() || destination > Adjacency_List.size()){
    //         System.out.println("the vertex entered in not present ");
    //         return;
    //     }
    //     List<Integer> slist = Adjacency_List.get(source);
    //     slist.add(destination);
    //     List<Integer> dlist = Adjacency_List.get(destination);
    //     dlist.add(source);
    // }

    /*
     * This method should return true if the Graph contains the vertex described by the input String.
     */
    public boolean containsVertex(String node) {
        //TODO: Implement function
        return false;
    }

    /*
     * This method should return true if there is a direct edge unlocked_from the vertex
     * represented by start String and end String.
     */
    public boolean containsEdge(String start, String end) {
        //TODO: Implement function
        return false;
    }

    /*
     * This method returns true if the house represented by the input String is locked
     * and false is the house has been left unlocked.
     */
    public boolean isLocked(String house) {
        //TODO: Implement function
        return false;
    }
}
