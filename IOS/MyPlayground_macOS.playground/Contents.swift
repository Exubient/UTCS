//: Playground - noun: a place where people can play

import Foundation

var str = "3"

str = "Hello, playground"

let str2 : String

str2 = "bye"


var a:(Int, Int) = (10, 3000)

a.0
a.1


var b:(String, String) = ("one", "two")

let f1:Float = 10

let f2:Double = 949

// You can never mix and match different data types!!!!

var f3 = Double(f1) + f2


//arguement tags for function parameters


//return types on the right side so the func is there


var age:Int? = 35

//unwrap the value of the optional class


var age2 = age

if age != nil{
    print("yes, unwrapped")
    print(age!)
}

if let tot = age {
    print(tot*2)
}

var someOptional:Int? = nil
var aDefaultValue:Int = 42

var the_answer = someOptional ?? aDefaultValue


//optionals!
func printName(name: String?) {
    guard let unwrappedName = name else {
        print("You need to provide a name.")
        return
    }
    print(unwrappedName)
}

//class inheritence
class Animal {
    var id:Int = 0
    init(id:Int) {
        self.id = id
    }
}
class Dog : Animal{
    var name:String = ""
    init(id: Int, name:String) {
        super.init(id: id)
        self.name = name
    }
}

var me = Dog.init(id: 1, name: "HENRY")
me.name
print(me.name)












