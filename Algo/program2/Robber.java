/**
 */

import java.util.ArrayList;
import java.util.Stack;


 
public class Robber {

    /*
     * This method should return true if the robber can rob all the houses in the neighborhood,
     * which are represented as a graph, and false if he cannot. The function should also print to the console the
     * order in which the robber should rob the houses if he can rob the houses. You do not need to print anything
     * if all the houses cannot be robbed.
     */
// https://sadakurapati.wordpress.com/tag/depth-first-search/ 참고하고 ㅎㅎ
    public static void graphDFSByStack(Node<String> source) {
        if (source == null) { return; }
        Stack<Node<String>> stack = new Stack<Node<String>>();
        //시작점 추가
        stack.push(source);
        while (!stack.isEmpty()) {
            Node<String> currentNode = stack.pop();
            visitNode(currentNode);
            currentNode.visited = true;
            //check if we reached out target node
            if (currentNode.equals(targetTreeNode)) {
                return; // we have found our target node V.
            }
            //add all of unvisited nodes to stack
            for (Node<String> neighbor : currentNode.neighbors) {
                if (!neighbor.visited) { stack.push(neighbor); }
            }
        }
    }


    public boolean canRobAllHouses(Graph neighborhood) {
        static Stack<String> stack= new Stack<String>();  
        // stack.add(node)
        // static class Node{
        //     String data;
        //     boolean visited;

        //     Node(String data){
        //         this.data = data
        //     }
        // }

        for (String name: Adjacency_List.keySet()){
            stack.add(neighborhood._unlocked)
        }
        stack.


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
