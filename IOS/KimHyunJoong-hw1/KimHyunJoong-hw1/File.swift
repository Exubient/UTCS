//
//  File.swift
//  KimHyunJoong-hw1
//
//  Created by Hyun Joong Kim on 1/23/17.
//  Copyright © 2017 Hyun Joong Kim. All rights reserved.
//



import Foundation

class Automobile {
    private var _make:String = ""
    private var _model:String = ""
    private var _numberOfDoors:Int = 0
    private var _speed:Int = 0
    
    init (_make:String, _model:String, _numberOfDoors:Int, _speed:Int){
        self._make = _make
        self._model = _model
        self._numberOfDoors = _numberOfDoors
        self._speed = _speed
    }
    
    class func create(_make:String, _model:String, _numberOfDoors:Int, _speed:Int) -> Automobile{
        return Automobile(_make:_make, _model:_model, _numberOfDoors:_numberOfDoors, _speed:_speed)
    }
    
    func set_make(_make:String){
        self._make = _make
    }
    
    func get_make() -> String{
        return self._make
    }
    
    func set_model(_model:String){
        self._model = _model
    }
    
    func get_model() -> String{
        return self._model
    }
    
    func set_numberOfDoors(_numberOfDoors:Int){
        self._numberOfDoors = _numberOfDoors
    }
    
    func get_numberOfDoors()->Int{
        return self._numberOfDoors
    }
    
    func get_speed() -> Int{
        return self._speed
    }
    
    func increaseSpeed(_speedChange:Int) -> Int{
        
        let _current = self._speed + _speedChange
        while (_current < 0) || (_current > 150){
            print("you have a problem")
            break
        }
        self._speed = _current
        return _current
    }
    
    func decreaseSpeed(_speedChange:Int) -> Int{
        
        let _current = self._speed - _speedChange
        while (_current < 0) || (_current > 150){
            print("you have a problem")
            break
        }
        self._speed = _current
        return _current
    }
    
    func description() -> String{
        let result1 = "Make: " + self._make
        let result2 = ", Model: " + self._model
        let result3 = ", NumDoors " + String(self._numberOfDoors)
        let result4 = ", Speed: " + String(self._speed)
        return result1 + result2 + result3 + result4
    }
    
    
    
}























