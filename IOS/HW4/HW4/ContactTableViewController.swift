//
//  MainTableViewController.swift
//  KimHyunJoong-HW4
//
//  Created by Hyun Joong Kim on 2/13/17.
//  Copyright © 2017 Hyun Joong Kim. All rights reserved.
//

import UIKit

class ContactViewController: UITableViewController {
    

    private var people = [Person]()
    
    public func createDataModel(){
        let p1 = Person(firstname: "Joe", lastname: "Johnson", age: 35, city: "TX", zip: 35, street: "1 Main Street", state: "TX")
        let p2 = Person(firstname: "Sam", lastname: "Smith", age: 27, city: "Falls", zip: 78228, street: "Main Street Marble", state: "TX")
        let p3 = Person(firstname: "Sue", lastname: "Jefferson", age: 52, city: "Houston", zip: 78328, street: "3 Main Stree", state: "TX")
        let p4 = Person(firstname: "Zoey", lastname: "Zimmerman", age: 17, city: "San Antonio", zip: 78428, street: "4 Main Street", state: "TX")
        let p5 = Person(firstname: "Alan", lastname: "Albright", age: 83, city: "Dallas", zip: 78528, street: "5 Main Street", state: "TX")
        let p6 = Person(firstname: "Chris", lastname: "Chambers", age: 33, city: "Round Rock", zip: 78628, street: "6 Main Street", state: "TX")
        let p7 = Person(firstname: "Danny", lastname: "Donaldon", age: 6, city: "Cedar Park", zip: 78728, street: "7 Main Street", state: "TX")
        let p8 = Person(firstname: "Eli", lastname: "Edgerton", age: 10, city: "Leander", zip: 78828, street: "8 Main Street", state: "TX")
        let p9 = Person(firstname: "Frank", lastname: "Farmer", age: 100, city: "Webster", zip: 78928, street: "9 Main Street", state: "TX")
        people = [p1, p2, p3, p4, p5, p6, p7, p8, p9]
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        createDataModel()
        //        self.navigationBar.topItem.title = "some title"
        
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    // MARK: - Table view data source
    
    override func numberOfSections(in tableView: UITableView) -> Int {
        return 1
    }
    
    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        // #warning Incomplete implementation, return the number of rows
        return 18
    }
    
    
    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        
        

        if indexPath.row % 2 == 0 { // runs if indexPath.row = 0, 2, 4, 6 etc
            let cell = tableView.dequeueReusableCell(withIdentifier: "nameCell", for: indexPath) as! NameTableViewCell
            cell.nameText.text = "Name"
            cell.firstnameText.text = people[indexPath.row/2].firstname
            cell.lastnameText.text = people[indexPath.row/2].lastname
            return cell
        } else { // runs if indexPath.row = 1, 3, 5, 7 etc
            let cell2 = tableView.dequeueReusableCell(withIdentifier: "addressCell", for: indexPath) as! AdressTableViewCell
            cell2.adressText.text = "Adress"
            cell2.cityText.text = people[(indexPath.row-1)/2].city
            cell2.stateText.text = people[(indexPath.row-1)/2].state
            cell2.streetText.text = people[(indexPath.row-1)/2].street
            let _age:String = String(describing: people[(indexPath.row-1)/2].age!)
            cell2.zipText.text = _age
            return cell2
        }
        
        
        }
    
    
}
