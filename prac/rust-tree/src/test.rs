#[cfg(test)]
mod tests_pointer_util {
    use std::cell::RefCell;
    use std::rc::Rc;
    use crate::ranked_tree::*;
    use crate::pointers_util::*;
    use super::*;

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
