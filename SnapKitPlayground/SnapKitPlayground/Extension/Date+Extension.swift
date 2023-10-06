//
//  Date+Extension.swift
//  yagunhaja
//
//  Created by 김성태 on 2022/12/06.
//

import Foundation

extension Date {
    var day: Int {
        Calendar.current.component(.day, from: self)
    }
}

extension Date {
    
    static func now() -> Date {
        return NSDate.now
    }
    
    func toString(format: String = "yyyy-MM-dd") -> String {
        let formatter = DateFormatter()
        formatter.dateStyle = .short
        formatter.dateFormat = format
        return formatter.string(from: self)
    }
    
    func toStringByKo(format: String = "yyyy-MM-dd\nHH:mm:dd") -> String {
        let formatter = DateFormatter()
        formatter.locale = Locale(identifier: "ko_KR")
        formatter.timeZone = TimeZone(abbreviation: "KST")
        formatter.dateStyle = .short
        formatter.dateFormat = format
        return formatter.string(from: self)
    }
    
    func dateToString(format: String = "yyyy-MM-dd") -> String {
        let formatter = DateFormatter()
        formatter.locale = Locale(identifier: "ko")
        formatter.dateStyle = .short
        formatter.dateFormat = format
        return formatter.string(from: self)
    }
    
    func daysOfMonth() -> Int {
        let calendar = Calendar.current
        let date = Date()
        guard let interval = calendar.dateInterval(of: .month, for: date) else { return -1 }
        guard let days = calendar.dateComponents([.day], from: interval.start, to: interval.end).day else { return -1 }
        return days
    }
    
    func days(_ targetDate: Date) -> Int {
        let cal = Calendar(identifier: .gregorian)
        let startDate = cal.startOfDay(for: self)
        let endDate = cal.startOfDay(for: targetDate)
        
        return cal.dateComponents([.day], from: startDate, to: endDate).day ?? 0
    }
    
    func hours(_ targetDate: Date) -> Int {
        let cal = Calendar.current
        
        return cal.dateComponents([.hour], from: self, to: targetDate).hour ?? 0
    }
    
    func addDay(_ day: Int) -> Date {
        Calendar.current.date(byAdding: .day, value: day, to: self) ?? self
    }
}


// 년, 월, 일
extension Date {
    func year() -> Int? {
        let calendar = Calendar.current
        let components = calendar.dateComponents([.year], from: self)
        return components.year
    }
    
    func month() -> Int? {
        let calendar = Calendar.current
        let components = calendar.dateComponents([.month], from: self)
        return components.month
    }
    
    func dayFromCalendar() -> Int? {
        let calendar = Calendar.current
        let components = calendar.dateComponents([.day], from: self)
        return components.day
    }
}


// date components to Date
func dateFromGivenNumber(
    year: Int = Date().year() ?? 0,
    month: Int = Date().month() ?? 0,
    day: Int = Date().dayFromCalendar() ?? 0,
    hr: Int = 0,
    min: Int = 0,
    sec: Int = 0
) -> Date? {
    var calendar = Calendar(identifier: .gregorian)
    calendar.timeZone = TimeZone(secondsFromGMT: 0)!
    let components = DateComponents(
        year: year,
        month: month,
        day: day,
        hour: hr,
        minute: min,
        second: sec
    )
    return calendar.date(from: components)
}
