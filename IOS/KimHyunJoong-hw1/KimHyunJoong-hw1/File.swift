//
//  File.swift
//  KimHyunJoong-hw1
//
//  Created by Hyun Joong Kim on 1/23/17.
//  Copyright © 2017 Hyun Joong Kim. All rights reserved.
//



//3. Get and set instance methods for each private property, except the speed property,
//which should only have a get method.
//4. A method named ‘increaseSpeed’, with one argument named ‘speedChange’ of
//integer type. Make sure the resulting speed is not outside the range of 0 to 150.
//5. A method named ‘decreaseSpeed’, with one argument named ‘speedChange’ of type
//integer. Make sure the resulting speed is not outside the range of 0 to 150.
//6. A method named ‘description’ that will return the following string:
//Make: <make>, Model: <model>, NumDoors: <number-of-doors>, Speed: <speed>
//2. In main.swift:
//1. Define a ‘main’ global-scope function, with no arguments. In this function:
//1. Create 3 Automobile objects with properties that produce the desired output (see
//item 3 below), using the create method.
//2. Define a loop that iterates 10 times, calling the increaseSpeed method on each
//Automobile object, passing in a random value that is returned from the
//randomValueBetween function (see below). Each call to increaseSpeed should use
//an argument value from a unique call to randomValueBetween. When calling the
//randomValueBetween function use minimum and maximum values of 0 and 16,
//respectively.
//3. After the loop has completed, call each object’s description method to output their
//final state.
//4. The last thing the main function should do is output a message for which automobile
//won the race, in this format: “<automobile make> <automobile model> won!!”. Or, in
//the unusual event there is a tie, output “There was a tie!”.
//1. Example: Honda Accord won!!
//2. At the global level, call the ‘main’ global-scope function.
//3. The output should look like this, with speed values probably different when your program
//runs:
//Make: Maserati, Model: GranTurismo, NumDoors: 2, Speed: 67
//Make: Honda, Model: Accord, NumDoors: 4, Speed: 128
//Make: Tesla, Model: S 90, NumDoors: 2, Speed: 35
//Honda Accord won!!
//4. Build and run the app, and verify the output is correct.
//
//


import Foundation

class Automobile {
    private var _name:String = ""
    private var _model:String = ""
    private var _numberOfDoors:Int = 0
    private var _speed:Int = 0
    
    init (_name:String, _model:String, _numberOfDoors:Int, _speed:Int){
        self._name = _name
        self._model = _model
        self._numberOfDoors = _numberOfDoors
        self._speed = _speed
    }
    
    class func create(_name:String, _model:String, _numberOfDoors:Int, _speed:Int) -> Automobile{
        return Automobile(_name:_name, _model:_model, _numberOfDoors:_numberOfDoors, _speed:_speed)
    }
    
    func set_name(_name:String){
        self._name = _name
    }
    
    func get_name() -> String{
        return self._name
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

    
    
}
















