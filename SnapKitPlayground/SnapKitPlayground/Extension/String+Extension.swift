//
//  String+Extension.swift
//  yagunhaja
//
//  Created by 김성태 on 2022/12/05.
//
import Foundation

extension String {
    var url: URL? {
        get {
            return URL(string: self)
        }
    }
    
    var urlEncode: String {
        get {
            guard let encodedStr = self.addingPercentEncoding(withAllowedCharacters: .urlQueryAllowed) else { return self }
            return encodedStr
        }
    }
}

extension String {
    func toDate(format: String) -> Date? {
        let dateFormatter = DateFormatter()
        dateFormatter.dateFormat = format
        dateFormatter.locale = Locale(identifier: "ko_KR")
        dateFormatter.timeZone = TimeZone(abbreviation: "KST")
        if let date = dateFormatter.date(from: self) {
            return date
        } else {
            return nil
        }
    }
}
