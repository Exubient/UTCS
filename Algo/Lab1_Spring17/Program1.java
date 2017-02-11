/*
 * Name: Hyun Joong Kim 
 * EID: hk23356
 */

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

/**
 * Your solution goes in this class.
 * 
 * Please do not modify the other files we have provided for you, as we will use
 * our own versions of those files when grading your project. You are
 * responsible for ensuring that your solution works with the original version
 * of all the other files we have provided for you.
 * 
 * That said, please feel free to add additional files and classes to your
 * solution, as you see fit. We will use ALL of your additional files when
 * grading your solution.
 */
public class Program1 extends AbstractProgram1 {
    /**
     * Determines whether a candidate Matching represents a solution to the
     * Stable Marriage problem. Study the description of a Matching in the
     * project documentation to help you with this.
     */

    public boolean isStableMatching(Matching marriage) {

        for(int worker = 0; worker < marriage.getWorkerCount(); worker++){
            //current match for the iteration of worker
            int jobMatch = marriage.getWorkerMatching().get(worker); 
            int indexOfWorker = marriage.getJobPreference().get(jobMatch).indexOf(worker);

            //let worker iterate smaller than the index of job preference of worker
            //and compute other workers to compare to current preference
            for(int worker_iteration = 0; worker_iteration < indexOfWorker ; worker_iteration++){ 
                int iter_worker = marriage.getJobPreference().get(jobMatch).get(worker_iteration);
                int iter_match = marriage.getWorkerMatching().get(iter_worker);
                int current_pref = marriage.getWorkerPreference().get(iter_worker).indexOf(jobMatch);
                int iter_pref = marriage.getWorkerPreference().get(iter_worker).indexOf(iter_match);
                if(iter_pref > current_pref){ return false ;}
            }
        }
        //if there is no problem cross referencing preferences, the solution is stable
        return true;
    }


    /**
     * Determines a solution to the Stable Marriage problem from the given input
     * set. Study the project description to understand the variables which
     * represent the input to your solution.
     * 
     * @return A stable Matching.
     */
    public Matching stableHiringGaleShapley(Matching marriage) {
        /* TODO implement this function */


}



