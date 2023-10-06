//
//  Array+Extension.swift
//  yagunhaja
//
//  Created by 정다연 on 2022/12/22.
//

import Foundation

extension Array {
    subscript (safe index: Int) -> Element? {
        return indices ~= index ? self[index] : nil
    }
}
