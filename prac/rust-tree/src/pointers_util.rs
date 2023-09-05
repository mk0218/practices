
/// Wrappers for Rc<RefCell<T>>
use std::cell::{ Ref, RefCell, RefMut };
use std::cmp::PartialEq;
use std::collections::VecDeque;
use std::collections::vec_deque::Iter;
use std::fmt;
use std::rc::{ Rc, Weak };
use crate::ranked_tree::RankedNode;

#[derive(Clone, Debug)]
pub struct Parent_<T>(pub Weak<RefCell<T>>);

#[derive(Clone)]
pub struct Child_<T>(pub Rc<RefCell<T>>);

pub struct Children_<T>(pub VecDeque<T>);

impl<T: fmt::Debug> fmt::Debug for Child_<T> {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "{:?}", *self.borrow())
    }
}

impl<T: fmt::Debug> fmt::Debug for Children_<T> {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "{:?}", self.0)
    }
}

impl<T> Parent_<T> {
    pub fn upgrade(&self) -> Child_<T> {
        Child_::<T>(self.0.upgrade().unwrap())
    }

    pub fn clone(p: &Parent_<T>) -> Parent_<T> {
        Parent_(Weak::clone(&p.0))
    }
}

impl<T> Child_<T> {
    pub fn new(node: T) -> Child_<T> {
        Child_::<T>(Rc::new(RefCell::new(node)))
    }

    pub fn downgrade(node: &Child_<T>) -> Parent_<T> {
        Parent_::<T>(Rc::downgrade(&node.0))
    }

    pub fn clone(c: &Child_<T>) -> Child_<T> {
        Child_(Rc::clone(&c.0))
    }
}

impl<'a, T> Child_<T> {
    pub fn borrow(&'a self) -> Ref<'a, T> {
        (*self.0).borrow()
    }

    pub fn borrow_mut(&'a self) -> RefMut<'a, T> {
        (*self.0).borrow_mut()
    }
}

impl<T: PartialEq> PartialEq for Child_<T> {
    fn eq(&self, other: &Self) -> bool {
        self.0 == other.0
    }
}

impl<T> Children_<T> {
    pub fn new() -> Children_<T> {
        Children_::<T>(VecDeque::new())
    }

    pub fn iter(&self) -> Iter<'_, T> {
        self.0.iter()
    }

    pub fn len(&self) -> usize {
        self.0.len()
    }

    pub fn is_empty(&self) -> bool {
        self.0.is_empty()
    }

    pub fn get(&self, index: usize) -> Option<&T> {
        self.0.get(index)
    }

    pub fn push_front(&mut self, node: T) {
        self.0.push_front(node);
    }

    pub fn push_back(&mut self, node: T) {
        self.0.push_back(node);
    }

    pub fn pop_front(&mut self) -> Option<T> {
        self.0.pop_front()
    }

    pub fn pop_back(&mut self) -> Option<T> {
        self.0.pop_back()
    }

    pub fn insert(&mut self, index: usize, node: T) {
        self.0.insert(index, node);
    }

    pub fn remove(&mut self, index: usize) -> Option<T> {
        self.0.remove(index)
    }
}

pub type Parent = Parent_<RankedNode>;
pub type Child = Child_<RankedNode>;
pub type Children = Children_<Child>;
