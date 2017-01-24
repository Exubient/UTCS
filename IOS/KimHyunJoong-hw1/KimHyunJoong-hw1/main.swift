//
//  main.swift
//  KimHyunJoong-hw1
//
//  Created by Hyun Joong Kim on 1/23/17.
//  Copyright © 2017 Hyun Joong Kim. All rights reserved.
//


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


func randomValueBetween(min:UInt32, max:UInt32) -> UInt32 {
    var randomValue:UInt32 = min + arc4random_uniform(UInt32(max - min + 1))
    return randomValue
}

func main() {
    var results:String=""

    var car1 = Automobile.create(_make: "HyunDai", _model: "Avante", _numberOfDoors: 4, _speed: 20)
    var car2 = Automobile.create(_make: "Audi", _model: "A8", _numberOfDoors: 4, _speed: 30)
    var car3 = Automobile.create(_make: "Kia", _model: "cheap_bike", _numberOfDoors: 2, _speed: 10)
    
    for count in 0 ..< 10{
        car1.increaseSpeed(_speedChange: Int(randomValueBetween(min: 0, max: 16)))
        car2.increaseSpeed(_speedChange: Int(randomValueBetween(min: 0, max: 16)))
        car3.increaseSpeed(_speedChange: Int(randomValueBetween(min: 0, max: 16)))
    }
    
    print(car1.description())
    print(car2.description())
    print(car3.description())
    
    
    let largest = max(car1.get_speed(), car2.get_speed(), car3.get_speed())

    if car1.get_speed() == largest{
        print(car1.get_make() + " " + car1.get_model() + " won!!")
    }
    else if car2.get_speed() == largest{
        print(car2.get_make() + " " + car2.get_model() + " won!!")
    }
    else{
        print(car3.get_make() + " " + car3.get_model() + " won!!")
    }
}

main()
