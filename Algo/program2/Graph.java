/**
 */

import java.io.IOException;
import java.io.FileReader;
import java.io.BufferedReader;


public class Graph {

    /*
     * Creates a graph to represent the neighborhood, where unlocked is the file name for the unlocked houses
     * and keys is the file name for which houses have which keys.
     */
    public Graph(String unlocked, String keys) {
        //TODO: Implement Constructor
        BufferedReader br = null;
        FileReader unlocked_fr = null;


        try {
            unlocked_fr = new FileReader(unlocked);
            br = new BufferedReader(unlocked_fr);

            String sCurrentLine;

            br = new BufferedReader(new FileReader(unlocked));

            while ((sCurrentLine = br.readLine()) != null) {
                System.out.println(sCurrentLine);
            }

        } catch (IOException e) {
            e.printStackTrace();

        } finally {
            try {
                if (br != null)
                    br.close();
                if (unlocked_fr != null)
                    unlocked_fr.close();
            } catch (IOException ex) {
                ex.printStackTrace();
            }
        }
    }


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
