//
//  dasdViewController.swift
//  KimHyunJoong-hw6
//
//  Created by Hyun Joong Kim on 3/1/17.
//  Copyright © 2017 Hyun Joong Kim. All rights reserved.
//

import UIKit

var pageViewController: UIPageViewController? = nil
let pageTitles = ["One", "Two", "Three"]


class PageViewController: UIPageViewController {
    
    override func viewDidLoad() {
        super.viewDidLoad()
        let viewController:UIViewController = UIStoryboard(name: "Main", bundle: nil).instantiateViewController(withIdentifier: "firstVC") as UIViewController
        // .instantiatViewControllerWithIdentifier() returns AnyObject! this must be downcast to utilize it
        
        self.present(viewController, animated: false, completion: nil)
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    
    /*
     // MARK: - Navigation
     
     // In a storyboard-based application, you will often want to do a little preparation before navigation
     override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
     // Get the new view controller using segue.destinationViewController.
     // Pass the selected object to the new view controller.
     }
     */
    
}
