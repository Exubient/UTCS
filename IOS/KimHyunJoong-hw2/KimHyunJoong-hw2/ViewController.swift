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
            _message.text = _name.text! + "  " + _city.text!
        }
        else{
            _message.text = "You must enter a value for *both* name and city!!"
        }
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()

        //background color
        _view.backgroundColor = UIColor.gray
        _button.backgroundColor = UIColor.orange
        _button.tintColor = UIColor.blue
        
        //no auto-fill
        _name.autocorrectionType = UITextAutocorrectionType.no
        _city.autocorrectionType = UITextAutocorrectionType.no
        
        //tapGestureUI
        let tap = UITapGestureRecognizer(target: self, action: #selector(self.func_tap))
        self.view.addGestureRecognizer(tap)
    }
    
    func func_tap(gesture: UITapGestureRecognizer) {
        _name.resignFirstResponder()
        _city.resignFirstResponder()
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}

