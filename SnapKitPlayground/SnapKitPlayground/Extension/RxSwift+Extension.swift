//
//  RxSwift+Extension.swift
//  yagunhaja
//
//  Created by 김성태 on 2022/12/06.
//

import RxSwift
import RxCocoa

extension ObservableType {
    func throttle(_ dueTime: RxTimeInterval = .milliseconds(300), isLatest: Bool = false, scheduler: SchedulerType = MainScheduler.instance) -> Observable<Element> {
        self.throttle(dueTime, latest: isLatest, scheduler: scheduler)
    }

    func throttle(_ dueTime: RxTimeInterval = .milliseconds(300), scheduler: SchedulerType = MainScheduler.instance) -> Observable<Element> {
        self.throttle(dueTime, latest: false, scheduler: scheduler)
    }

    func debounce(_ dueTime: RxTimeInterval = .milliseconds(300)) -> Observable<Element> {
        self.debounce(dueTime, scheduler: MainScheduler.instance)
    }
}
