//
//  ViewController.swift
//  KimHyunJoong-hw2
//
//  Created by Hyun Joong Kim on 1/30/17.
//  Copyright © 2017 Hyun Joong Kim. All rights reserved.
//

import UIKit

class ViewController: UIViewController{
    @IBOutlet var _view: UIView!
    @IBOutlet weak var _name: UITextField!
    @IBOutlet weak var _city: UITextField!
    @IBOutlet weak var _button: UIButton!
    @IBOutlet weak var _message: UILabel!

    
    @IBAction func button_tap(_ sender: Any) {
        if _name.text != "" && _city.text != ""{
            _message.text = _name.text! + _city.text!
        }
        else{
            _message.text = "need to write both"
        }
    }
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.

        _name.autocorrectionType = UITextAutocorrectionType.no
        _city.autocorrectionType = UITextAutocorrectionType.no
        _view.backgroundColor = UIColor.gray
        
//        let tapGesture = UITapGestureRecognizer(target: self, action: "tap:")
//        view.addGestureRecognizer(tapGesture)
        
        //tapGestureUI
        let tap = UITapGestureRecognizer(target: self, action: #selector(self.func_tap))
        self.view.addGestureRecognizer(tap)
        
    }
    
    func func_tap(gesture: UITapGestureRecognizer) {
        _name.resignFirstResponder()
        _name.resignFirstResponder()
        
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}

