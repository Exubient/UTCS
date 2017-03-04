/**
 */

import java.io.IOException;
import java.io.FileReader;
import java.io.BufferedReader;

import java.util.HashMap;
import java.util.LinkedList;
import java.util.ArrayList;
import javafx.util.Pair;
import java.util.List;
import java.util.Map;


public class Graph {
    private List<String> _unlocked = new ArrayList<String>();
    private Map<String,List<String>> Adjacency_List = new HashMap<String, List<String>>(); 
    private Map<String,List<String>> Adjacency_List_bool = new HashMap<String, List<String>>(); 

    public Graph(String unlocked, String keys) {
        read(unlocked);
        read(keys);
        
        this.Adjacency_List = Adjacency_List;
        this._unlocked = _unlocked;
        for(String name: _unlocked){
            System.out.println(name);
        }
        //output the graph
        for (String name: Adjacency_List.keySet()){
            String value = Adjacency_List.get(name).toString();  
            System.out.println(name + " " + value);  
        } 
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
                    _unlocked.add(sCurrentLine);
                }
            }

            else { 
                while ((sCurrentLine = br.readLine()) != null) {
                    List<String> tmp_list = new ArrayList<String>();
                    String[] parts = sCurrentLine.split(":");
                    if (parts.length > 1) {
                        String[] edges = sCurrentLine.split(",");
                        for(String word:parts[1].substring(1).split(", ")){  
                            tmp_list.add(word); 
                        }
                    }
                    Adjacency_List.put(parts[0], new ArrayList<String>(tmp_list));
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
    /*
     * This method should return true if the Graph contains the vertex described by the input String.
     */
    public boolean containsVertex(String node) {
        if(Adjacency_List.containsKey(node)){
            return true;
        }
        else{
            return false;
        }
    }

    /*
     * This method should return true if there is a direct edge unlocked_from the vertex
     * represented by start String and end String.
     */
    public boolean containsEdge(String start, String end) {
        for (String key: Adjacency_List.keySet()){
            if(Adjacency_List.containsKey(start) && Adjacency_List.get(start).contains(end)){ 
                return true;
                }
            } 
            return false;
    }

    /*
     * This method returns true if the house represented by the input String is locked
     * and false is the house has been left unlocked.
     */
    public boolean isLocked(String house) {
        //TODO: Implement function
        if (_unlocked.contains(house)){
            return false;
        }
        return true;
    }
}
