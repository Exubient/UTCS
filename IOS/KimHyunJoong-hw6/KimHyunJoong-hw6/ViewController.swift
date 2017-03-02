//
//  ViewController.swift
//  KimHyunJoong-hw6
//
//  Created by Hyun Joong Kim on 2/27/17.
//  Copyright © 2017 Hyun Joong Kim. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    @IBOutlet weak var image: UIImageView!
    var pageIndex: Int = 0
    var strTitle: String!
    var strPhotoName: String!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        
        
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func viewWillAppear(_ animated: Bool) {
        image.image = UIImage(named: "img_1.png")

    }
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}

