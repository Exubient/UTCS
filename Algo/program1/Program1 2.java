/*
 * Name: Kausthub Poondi
 * EID: kp26753
 */

import java.util.ArrayList;
import java.util.LinkedList;

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
        /*
         * Obtains the necessary information from the Matching object passed into the function
         */
        int numJobs = marriage.getJobCount();
        int numWorkers = marriage.getWorkerCount();

        ArrayList<ArrayList<Integer>> jobPreference = marriage.getJobPreference();
        ArrayList<ArrayList<Integer>> workerPreference =  marriage.getWorkerPreference();
        ArrayList<Integer> matchings = marriage.getWorkerMatching();

        /* 
         *Loops through every single pair in the given Matching and checks to 
         * see if any two pairs have an instability. 
         */
        for(int i = 0; i < numJobs; i++) {
            int baseWorker = i;
            Integer baseCompany = matchings.get(i);

            /*
             *Compares the baseWorker and baseCompany to another macthing in the give
             * set to check for an instability.
             */
            for(int k = i + 1; k < numJobs; k++) {
                int compareWorker = k;
                int compareCompany = matchings.get(k);

                /*
                 * Finds how each worker and each company rankes the other two companies 
                 * and workers respectively. Stores the rankking into variables for checking.
                 */
                int baseWorker_baseCompany = workerPreference.get(baseWorker).indexOf(baseCompany);
                int baseWorker_compareCompany = workerPreference.get(baseWorker).indexOf(compareCompany);


                int compareWorker_baseCompany = workerPreference.get(compareWorker).indexOf(baseCompany);
                int compareWorker_compareCompany = workerPreference.get(compareWorker).indexOf(compareCompany); 

                int baseCompany_baseWorker = jobPreference.get(baseCompany).indexOf(baseWorker);
                int baseCompany_compareWorker = jobPreference.get(baseCompany).indexOf(compareWorker);

        
                int compareCompany_baseWorker = jobPreference.get(compareCompany).indexOf(baseWorker);
                int compareCompany_compareWorker = jobPreference.get(compareCompany).indexOf(compareWorker);

                /* 
                 * Compares the ranking obtained to determine if an instability exists
                 */
                if((baseWorker_compareCompany < baseWorker_baseCompany) && 
                    (compareCompany_baseWorker < compareCompany_compareWorker)) {
                    return false;
                }
                else if((compareWorker_baseCompany < compareWorker_compareCompany) && 
                    (baseCompany_compareWorker < baseCompany_baseWorker)) {
                    return false;
                }
            }        
        }
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
        /*
         * Obtains the necessary information from the Matching object passed into the function
         */
        int numWorkers = marriage.getJobCount();
        int numJobs = marriage.getWorkerCount();


        ArrayList<ArrayList<Integer>> jobPreference = marriage.getJobPreference();
        ArrayList<ArrayList<Integer>> workerPreference = marriage.getWorkerPreference();

        /*
         * Creates extra ArrayLists and LinkedList in order to copy and store necessary information
         * for the execution of the GS algorithim below. 
         */
        ArrayList<ArrayList<Integer>> reverse_jobPreference = new ArrayList<ArrayList<Integer>>();
         ArrayList<ArrayList<Integer>> copy_workerPreference = new ArrayList<ArrayList<Integer>>();

        ArrayList<Integer> reverse_matchings = new ArrayList<Integer>();
        ArrayList<Integer> matchings = new ArrayList<Integer>();

        LinkedList<Integer> worker_list = new LinkedList<Integer>();

        /* Initializes the reverse_jobPreference and copy_workerPreference 2D lists
         * to -1 so they can be altered with real data further in the execution. 
         */
        for (int i = 0; i < numJobs; i++) {
            ArrayList<Integer> worker = new ArrayList<Integer>();
            ArrayList<Integer> job = new ArrayList<Integer>();

            reverse_jobPreference.add(job);
            copy_workerPreference.add(worker);

            for(int k = 0; k < numJobs; k++) {
                worker.add(-1);
                job.add(-1);
            }
        }
        
        /* 
         * Makes a copy of the workerPreference 2D list and creates an inverse copy of the jobPreference 
         * 2D list where in each row, the indexes become the values and the value become the indexes. 
         * This is done in order to reduce the search time in the algorithm. 
         */
        for(int i = 0; i < numJobs; i++) {
            for(int k = 0; k < numWorkers; k++) {
                reverse_jobPreference.get(i).set(jobPreference.get(i).get(k), k);
                copy_workerPreference.get(i).set(k, workerPreference.get(i).get(k));
            }
        }

        /*
         * Makes a LinkedList of all the workers in to simulate a "queue".
         * Allows the algorithm to add and remove men from the queue as 
         * are hired or let go. Also creates a list of matchings from worker
         * to job and job to worker.
         */
        for (int i = 0; i < numWorkers; i++) {
            worker_list.add(jobPreference.get(0).get(i));
            reverse_matchings.add(-1);
            matchings.add(-1);
        }

        /*
         * Implementation of the actual Gale-Shapley algorithm that keeps running 
         * until the "queue" of workers is empty.
         */
        while (worker_list.size() != 0) {
            /*
             * Obtains the first worker from the list an removes him/her from the queue.
             * Finds the first job on his/her preference list and removes it. 
             */
            int main_worker = worker_list.getFirst();
            worker_list.removeFirst();

            int main_job = copy_workerPreference.get(main_worker).get(0);
            copy_workerPreference.get(main_worker).remove(0);

            /* 
             * Checks to see if the job has not been matched. If it has not,
             * then creates a match between main_man and main_worker. If not, 
             * uses inverted job preference list in order to find the appropriate 
             * rankings. 
             */ 
            if(reverse_matchings.get(main_job) == -1) {
                reverse_matchings.set(main_job, main_worker);
                matchings.set(main_worker, main_job);
            }
            else {
                int current_worker = reverse_matchings.get(main_job);
                int rank_current_worker = reverse_jobPreference.get(main_job).get(current_worker);
                int rank_main_worker = reverse_jobPreference.get(main_job).get(main_worker);

                /*
                 * Makes a comparison on how main_job rankes compares curret_worker to 
                 * main_worker. If the ranking for main_worker is higher, current_worker is let go
                 * and added back to the queue. If not, the main_worker remains free.
                 */
                if(rank_main_worker < rank_current_worker) {
                    reverse_matchings.set(main_job, main_worker);
                    matchings.set(main_worker, main_job);
                    worker_list.addLast(current_worker);
                }
                else {
                    worker_list.addLast(main_worker);
                }
            }
        }

        marriage.setWorkerMatching(matchings);
        return marriage; 
    }
}

