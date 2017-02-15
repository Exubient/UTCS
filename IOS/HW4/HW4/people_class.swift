//
//  people_class.swift
//  HW4
//
//  Created by Hyun Joong Kim on 2/15/17.
//  Copyright © 2017 Hyun Joong Kim. All rights reserved.
//

import Foundation

class Person {
    public var firstname:String?
    public var lastname:String?
    public var age:Int?
    public var street:String?
    public var city:String?
    public var state:String?
    public var zip:Int?
    
    init (firstname:String , lastname:String, age:Int, city:String, zip:Int, street:String, state:String){
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip
        
    }
}
