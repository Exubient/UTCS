package assignment1;
/*
 *  * Name: <your name>
 *   * EID: <your EID>
 *    */

import java.util.ArrayList;
import java.util.HashMap;

//import com.sun.xml.internal.bind.v2.schemagen.xmlschema.List;
//
///**
// * Your solution goes in this class.
//  * 
//   * Please do not modify the other files we have provided for you, as we will use
//    * our own versions of those files when grading your project. You are
//     * responsible for ensuring that your solution works with the original version
//      * of all the other files we have provided for you.
//       * 
//        * That said, please feel free to add additional files and classes to your
//         * solution, as you see fit. We will use ALL of your additional files when
//          * grading your solution.
//           */
//           public class Program1 extends AbstractProgram1 {
//               /**
//                    * Determines whether a candidate Matching represents a solution to the
//                         * Stable Marriage problem. Study the description of a Matching in the
//                              * project documentation to help you with this.
//                                   */
//                                       public boolean isStableMatching(Matching marriage) {
//                                               /* TODO implement this function */
//														ArrayList<Integer> final_matching = marriage.getWomenMatching();
//																ArrayList<Integer> men_preferences, women_preferences;
//																		for(int i = 0; i < final_matching.size(); i++){ // iterates through women in matching
//																					int m = final_matching.get(i); // get man matched to woman
//																								if(m == -1){return false;}
//																											women_preferences = marriage.getWomenPreference().get(i); // gets woman's preference list
//																														for(int other_m = 0; other_m < women_preferences.size(); other_m++){
//																																		if(women_preferences.get(other_m) < women_preferences.get(m)){
//																																							men_preferences = marriage.getMenPreference().get(other_m);
//																																												if(men_preferences.get(i) < men_preferences.get(final_matching.indexOf(other_m))){
//																																																		return false;
//																																																							}
//																																																											}
//																																																														}
//																																																																}
//																																																																		
//																																																																		        return true;
//																																																																		            }
//
//																																																																		                /**
//																																																																		                     * Determines a solution to the Stable Marriage problem from the given input
//																																																																		                          * set. Study the project description to understand the variables which
//																																																																		                               * represent the input to your solution.
//																																																																		                                    * 
//																																																																		                                         * @return A stable Matching.
//																																																																		                                              */
//																																																																		                                                  public Matching stableMarriageGaleShapley(Matching marriage) {
//																																																																		                                                          /* TODO implement this function */
//																																																																																		ArrayList<HashMap<Integer, ArrayList<Integer>>> men_preferences = new ArrayList<HashMap<Integer, ArrayList<Integer>>>(0);
//																																																																																				ArrayList<HashMap<Integer, ArrayList<Integer>>> women_preferences = new ArrayList<HashMap<Integer, ArrayList<Integer>>>(0);
//																																																																																						ArrayList<Integer> final_matching = new ArrayList<Integer>(0);
//																																																																																								for(Integer i = 0; i < marriage.getMenPreference().size(); i++){
//																																																																																											final_matching.add(-1);
//																																																																																														men_preferences.add(new HashMap<Integer, ArrayList<Integer>>(0));
//																																																																																																	women_preferences.add(new HashMap<Integer, ArrayList<Integer>>(0));
//																																																																																																				for(int p = 0; p < marriage.getMenPreference().get(i).size(); p++){
//																																																																																																								if(!men_preferences.get(i).containsKey(marriage.getMenPreference().get(i).get(p))){
//																																																																																																													men_preferences.get(i).put(marriage.getMenPreference().get(i).get(p), new ArrayList<Integer>());
//																																																																																																																		men_preferences.get(i).get(marriage.getMenPreference().get(i).get(p)).add(p);
//																																																																																																																						}else{
//																																																																																																																											men_preferences.get(i).get(marriage.getMenPreference().get(i).get(p)).add(p);
//																																																																																																																															}
//																																																																																																																																			if(!women_preferences.get(i).containsKey(marriage.getWomenPreference().get(i).get(p))){
//																																																																																																																																								women_preferences.get(i).put(marriage.getWomenPreference().get(i).get(p), new ArrayList<Integer>());
//																																																																																																																																													women_preferences.get(i).get(marriage.getWomenPreference().get(i).get(p)).add(p);
//																																																																																																																																																	}else{
//																																																																																																																																																						women_preferences.get(i).get(marriage.getWomenPreference().get(i).get(p)).add(p);
//																																																																																																																																																										}
//																																																																																																																																																													}
//																																																																																																																																																															}
//																																																																																																																																																																	marriage.setWomanMatching(final_matching);
//																																																																																																																																																																			int w;
//																																																																																																																																																																					int max = marriage.totalMenCount();
//																																																																																																																																																																							for(int m = 0; m < max; m++){
//																																																																																																																																																																										int rank = 1;
//																																																																																																																																																																													while(rank < max){
//																																																																																																																																																																																	if(men_preferences.get(m).containsKey(rank) && men_preferences.get(m).get(rank).size() != 0)
//																																																																																																																																																																																						w = men_preferences.get(m).get(rank).remove(men_preferences.get(m).get(rank).size() - 1);
//																																																																																																																																																																																										else{rank++;continue;}
//																																																																																																																																																																																														if(marriage.getWomenMatching().indexOf(m) != -1){ rank++; continue; }
//																																																																																																																																																																																																		int other_m = marriage.getWomenMatching().get(w);
//																																																																																																																																																																																																						if(marriage.getWomenMatching().get(w) == -1 ||
//																																																																																																																																																																																																												marriage.getWomenPreference().get(w).get(m) < marriage.getWomenPreference().get(w).get(other_m)){
//																																																																																																																																																																																																																	marriage.getWomenMatching().set(w, m);
//																																																																																																																																																																																																																						break;
//																																																																																																																																																																																																																										}
//																																																																																																																																																																																																																														if(men_preferences.get(m).get(rank).size() == 0)
//																																																																																																																																																																																																																																			rank++;
//																																																																																																																																																																																																																																						}
//																																																																																																																																																																																																																																									if(m == max - 1){
//																																																																																																																																																																																																																																													if(marriage.getWomenMatching().indexOf(-1) != -1){m = -1;}
//																																																																																																																																																																																																																																																}
//																																																																																																																																																																																																																																																		}
//																																																																																																																																																																																																																																																		        return marriage;
//																																																																																																																																																																																																																																																		            }
//																																																																																																																																																																																																																																																		            }
