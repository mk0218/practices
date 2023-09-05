use std::cell::RefCell;
use std::collections::VecDeque;
use std::rc::Rc;
use crate::pointers_util::*;
use crate::ranked_tree::*;

pub fn add(left: usize, right: usize) -> usize {
    left + right
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        let result = add(2, 2);
        assert_eq!(result, 4);
    }

    #[test]
    fn parent_upgrade() {
        let value = Rc::new(RefCell::new(String::from("value")));
        let parent = Parent_(Rc::downgrade(&value));
        let child = Child_(value);
        assert_eq!(parent.upgrade(), child);
    }

    #[test]
    fn parent_upgrade_node() {
        let value = Rc::new(RefCell::new(RankedNode::Root {
            id: 0,
            children: Children::new(),
        }));
        let parent = Parent_(Rc::downgrade(&value));
        let child = Child_(value);
        assert_eq!(parent.upgrade(), child);
    }

    #[test]
    fn child_borrow() {
        let value = Rc::new(RefCell::new(RankedNode::Root {
            id: 0,
            children: Children::new(),
        }));
        let child = Child_(Rc::clone(&value));
        let child_borrow = child.borrow();
        assert_eq!(*child_borrow, *(*value).borrow());
    }

    #[test]
    fn child_clone() {
        let value = Rc::new(RefCell::new(RankedNode::Root {
            id: 0,
            children: Children::new(),
        }));
        let child = Child_(value);
        let cloned = Child_::clone(&child);
        assert_eq!(*(*child.0).borrow(), *(*cloned.0).borrow());
    }
}
