/**
 */

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.Stack;

 
public class Robber {

    /*
     * This method should return true if the robber can rob all the houses in the neighborhood,
     * which are represented as a graph, and false if he cannot. The function should also print to the console the
     * order in which the robber should rob the houses if he can rob the houses. You do not need to print anything
     * if all the houses cannot be robbed.
     */
// https://sadakurapati.wordpress.com/tag/depth-first-search/ 참고하고 ㅎㅎ

    class Node<T> {
        T data;
        ArrayList<Node<T>> neighbors = null;
        boolean visited = false;

        Node(T value) {
            data = value;
            neighbors = new ArrayList<Node<T>>();
        }

    }




    public static boolean graphDFSByStack(Graph neighborhood) {

                // declare Graph as class Node
        Node<String> A = new Node<String>("House A");
        Node<String> B = new Node<String>("House B");
        Node<String> C = new Node<String>("House C");
        Node<String> D = new Node<String>("House D");

        Stack<Node<String>> stack = new Stack<Node<String>>();        
        //start point(one for now)
        System.out.println(A.data);
        return true;
        // for(String name: neighborhood._unlocked){
        //     String source = name;    
        // }
        // if (source == null) { return false; }
        // stack.push(source);
        // while (!stack.isEmpty()) {
        //   Node<String> currentNode = stack.pop();
        //   visitNode(currentNode);
        //   currentNode.visited = true;
        //   //check if we reached out target node
        //   if (currentNode.equals(targetTreeNode)) {
        //     return; // we have found our target node V.
        //   }
        //   //add all of unvisited nodes to stack
        //   for (Node<String> neighbor : currentNode.neighbors) {
        //     if (!neighbor.visited) {
        //       stack.push(neighbor);
        //     }
        //   }
        // }
    }


    public boolean canRobAllHouses(Graph neighborhood) {



        boolean var = graphDFSByStack(neighborhood); 
        // else return false


        // for (String name: Adjacency_List.keySet()){
        //     stack.add(neighborhood._unlocked);
        // }
        // // stack.
        return false;
    }

    /*
     *
     */
    public void maximizeLoot(String lootList) {
        //TODO: Implement Function

    }


    public void scheduleMeetings(String buyerList) {
        //TODO: Implement Function

    }
}
