//
//  AdressTableViewCell.swift
//  HW4
//
//  Created by Hyun Joong Kim on 2/15/17.
//  Copyright © 2017 Hyun Joong Kim. All rights reserved.
//

import UIKit

class AdressTableViewCell: UITableViewCell {
    @IBOutlet weak var adressText: UILabel!
    @IBOutlet weak var streetText: UILabel!
    @IBOutlet weak var cityText: UILabel!
    @IBOutlet weak var stateText: UILabel!
    @IBOutlet weak var zipText: UILabel!

    override func awakeFromNib() {
        super.awakeFromNib()
        // Initialization code
    }

    override func setSelected(_ selected: Bool, animated: Bool) {
        super.setSelected(selected, animated: animated)

        // Configure the view for the selected state
    }

}
