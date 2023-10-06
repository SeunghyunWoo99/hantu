//
//  UIView+Extension.swift
//  yagunhaja
//
//  Created by 김성태 on 2022/12/16.
//

import Foundation
import UIKit

extension UIView {
    
    var cornerRadius: CGFloat {
        get {
            layer.cornerRadius
        }
        set {
            layer.cornerRadius = newValue
            layer.masksToBounds = newValue > 0
        }
    }
    
}
