//
//  UIColor+Extension.swift
//  yagunhaja
//
//  Created by Aiden on 2022/12/16.
//

import UIKit

extension UIColor {
    /// RGB가 각각 `red`, `green`, `blue`이고 opacity는 `a`인 Color object 반환
    convenience init(red: Int, green: Int, blue: Int, a: CGFloat = 1.0) {
        self.init(red: CGFloat(red) / 255.0,
                  green: CGFloat(green) / 255.0,
                  blue: CGFloat(blue) / 255.0,
                  alpha: a
        )
    }
}

extension UIColor {
    /// RGB가 `hex`, opacity는 1에 해당하는 Color object 반환
    convenience init(hex: Int) {
        self.init(
            red: (hex >> 16) & 0xff,
            green: (hex >> 8) & 0xff,
            blue: hex & 0xff
        )
    }
}

extension UIColor {
    /// RGB(22, 22, 22)
    class var gray_222222: UIColor { return UIColor(hex: 0x222222)}
}
