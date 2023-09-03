use std::cell::RefCell;
use std::rc::{ Rc, Weak };

pub struct RankedTree(RefCell<Rc<N>>, usize);

pub enum RankedNode {
    Root {
        id: usize,
        children: Vec<Rc<RefCell<N>>>,
    },
    Node {
        id: usize,
        rank: usize,
        parent: Weak<RefCell<N>>,
        children: Vec<Rc<RefCell<N>>>,
    },
}

type N = RankedNode;

impl PartialEq for RankedNode {
    fn eq(&self, other: &Self) -> bool {
        self.id() == other.id()
    }
}

impl RankedNode {
    fn id(&self) -> usize {
        match self {
            N::Root { id, .. } | N::Node { id, .. } => *id
        }
    }

    fn rank(&self) -> Option<usize> {
        match self {
            N::Root { .. } => None,
            N::Node { rank, .. } => Some(*rank)
        }
    }

    fn parent(&self) -> Option<Weak<RefCell<N>>> {
        match self {
            N::Root { .. } => None,
            N::Node { parent, .. } => Some(Weak::clone(parent)),
        }
    }

    fn add_child(&mut self, child: Rc<RefCell<N>>) {
        match self {
            N::Root { children, .. } |
            N::Node { children, .. } => {
                children.push(child)
            },
        }
    } 
}

impl RankedTree {
    pub fn new() -> RankedTree {
        RankedTree(RefCell::new(Rc::new(N::Root {   
            id: 0,
            children: vec![],
        })), 1)
    }

    fn next_id(&mut self) -> usize {
        self.1 += 1;
        return self.1 - 1;
    }
}
