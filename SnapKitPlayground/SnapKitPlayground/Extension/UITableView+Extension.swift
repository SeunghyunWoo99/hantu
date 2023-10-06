//
//  UITableView+Extension.swift
//  yagunhaja
//
//  Created by 정다연 on 2022/12/16.
//

import UIKit

extension UITableView {
    //  Generics USE (C++ Template과 같은 기능)
    func register<T: UITableViewCell>(_ className: T.Type) {
        let cellName = String(describing: T.self)
        // xib/nib이 없는 셀에서 사용하던 register(with:) 제거
        if Bundle.main.path(forResource: cellName, ofType: "nib") == nil {
            register(T.self, forCellReuseIdentifier: cellName)
            return
        }
        let nib = UINib(nibName: cellName, bundle: nil)
        register(nib, forCellReuseIdentifier: String(describing: cellName))
    }

    func register<T: UITableViewHeaderFooterView>(_ className: T.Type) {
        let cellName = String(describing: T.self)
        let nib = UINib(nibName: cellName, bundle: nil)
        register(nib, forHeaderFooterViewReuseIdentifier: String(describing: cellName))
    }
}

extension UITableView {
    func dequeueReusableCell<T: UITableViewCell>(withClass name: T.Type) -> T {
        guard let cell = dequeueReusableCell(withIdentifier: String(describing: name)) as? T else {
            fatalError("Couldn't find UITableViewCell for \(String(describing: name))")
        }
        return cell
    }

    func dequeueReusableCell<T: UITableViewCell>(withClass name: T.Type, for indexPath: IndexPath) -> T {
        guard let cell = dequeueReusableCell(withIdentifier: String(describing: name), for: indexPath) as? T else {
            fatalError("Couldn't find UITableViewCell for \(String(describing: name))")
        }
        return cell
    }
}
