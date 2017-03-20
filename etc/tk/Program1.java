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
            int indexOfJob = marriage.getWorkerPreference().get(worker).get(jobMatch);

            //let worker iterate smaller than the index of job preference of worker
            //and compute other workers to compare to current preference
            for(int worker_iteration = 0; worker_iteration < marriage.getWorkerCount() ; worker_iteration++){ 
                int iter_match = marriage.getWorkerMatching().get(worker_iteration);
                int current_pref = marriage.getWorkerPreference().get(worker).get(iter_match);
                int iter_pref = marriage.getJobPreference().get(iter_match).get(worker);
                int iter_pref2 = marriage.getJobPreference().get(iter_match).get(worker_iteration);
                //check for strong instability
                if((current_pref < indexOfJob) && (iter_pref < iter_pref2)) { return false; } 
                //check for weak instability
                else if((current_pref == indexOfJob) && (iter_pref < iter_pref2)) { return false; }
                else if((current_pref < indexOfJob) && (iter_pref == iter_pref2)) { return false; } 
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
        ArrayList<Integer> Worker_set = new ArrayList<Integer>();   
        ArrayList<Integer> job_set = new ArrayList<Integer>();    
        ArrayList<Integer> index_ordered = new ArrayList<Integer>(); // ordered arraylist of preference 


        int worker, job, index, current_index, current_pref, new_pref, ordered_index; 

        for( worker= 0; worker < marriage.getJobCount(); worker++) {
            job_set.add(-1);
            Worker_set.add(worker);
        }

        while( Worker_set.size() != 0) {
            job = Worker_set.get(0); //first worker

            for(index = 0; index < marriage.getJobCount(); index++) {
                for(worker = 0; worker < marriage.getJobCount(); worker++) {
                    if(marriage.getWorkerPreference().get(job).get(worker) == index) {
                        index_ordered.add(worker);
                    }
                }
            }

            while(index_ordered.size() != 0) {

                ordered_index = index_ordered.get(0);
                current_index = job_set.get(ordered_index);
                if(current_index == -1) {
                    job_set.set(ordered_index, job);
                    Worker_set.remove(0);
                    break;
                 // engaged with someone
                } else {
                    current_pref = marriage.getJobPreference().get(ordered_index).get(job);  //job preference 
                    new_pref = marriage.getJobPreference().get(ordered_index).get(current_index); //job preference  
                    // give up 

                    if(current_pref > new_pref) {
                        index_ordered.remove(0);
                        continue;

                    // cannot make a decision now
                    } else if(current_pref == new_pref) {
                        // check worker's preference about proposed job
                        current_pref = marriage.getWorkerPreference().get(job).get(ordered_index);
                        new_pref = marriage.getWorkerPreference().get(current_index).get(ordered_index);

                        // the man likes more
                        if(current_pref > new_pref) {
                            index_ordered.remove(0);
                            continue;
                        // proposing man likes more
                        } else if(current_pref < new_pref){
                            job_set.set(ordered_index, job);
                            Worker_set.remove(0);
                            Worker_set.add(current_index);
                            break;
                         // perfectly same state
                         // if we didn't leave that couple, it can't be ended
                        } else {
                            index_ordered.remove(0);
                            continue;
                        }
                    // take that job
                    } else {
                        job_set.set(ordered_index, job);
                        Worker_set.remove(0);
                        Worker_set.add(current_index);
                        break;
                    }
                }
            }
            index_ordered.clear();
        }

        for(worker=0; worker < marriage.getWorkerCount(); worker++) {
            Worker_set.add(-1);
        }

        for(worker=0; worker < marriage.getWorkerCount(); worker++) {
            Worker_set.set(job_set.get(worker), worker);
        }


        marriage.setWorkerMatching(Worker_set);
        return marriage;
    }
}