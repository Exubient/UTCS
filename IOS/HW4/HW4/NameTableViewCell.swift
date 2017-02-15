//
//  NameTableViewCell.swift
//  HW4
//
//  Created by Hyun Joong Kim on 2/15/17.
//  Copyright © 2017 Hyun Joong Kim. All rights reserved.
//

import UIKit

class NameTableViewCell: UITableViewCell {

    @IBOutlet weak var nameText: UILabel!
    @IBOutlet weak var firstnameText: UILabel!
    @IBOutlet weak var lastnameText: UILabel!
    @IBOutlet weak var detailButton: UIButton!
    override func awakeFromNib() {
        super.awakeFromNib()
        // Initialization code
    }

    override func setSelected(_ selected: Bool, animated: Bool) {
        super.setSelected(selected, animated: animated)

        // Configure the view for the selected state
    }

}
