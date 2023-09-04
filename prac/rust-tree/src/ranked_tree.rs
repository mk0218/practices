use std::cell::RefCell;
use std::cmp::Ordering;
use std::collections::{ HashMap, VecDeque };
use std::fmt;
use std::rc::{ Rc, Weak };

pub struct RankedTree(HashMap<usize, Rc<RefCell<N>>>, usize);

pub enum RankedNode {
    Root {
        id: usize,
        children: VecDeque<Rc<RefCell<N>>>,
    },
    Node {
        id: usize,
        rank: usize,
        parent: Weak<RefCell<N>>,
        children: VecDeque<Rc<RefCell<N>>>,
    },
}

type N = RankedNode;        

impl PartialEq for RankedNode {
    fn eq(&self, other: &Self) -> bool {
        self.id() == other.id()
    }
}

impl PartialOrd for RankedNode {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        match (self.rank(), other.rank()) {
            (Some(r1), Some(r2)) => r1.partial_cmp(&r2),
            _ => None,
        }
    }
}

impl fmt::Debug for RankedTree {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "RankedTree (")?;
        self.0.iter().fold(Ok(()), |_acc, n| {
            let (id, reference) = n;
            let rf = (*reference).borrow();
            if let Some(rank) = &rf.rank() {
                write!(f, " {}: (id: {}, rank: {}) ", id, &rf.id(), rank)
            } else {
                write!(f, " {}: (id: {}, rank: Root) ", id, &rf.id())
            }
        })?;
        write!(f, ")")
    }
}

impl fmt::Debug for RankedNode {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            N::Root { children, .. } => {
                write!(f, "Root ( ")?;
                for (i, c) in children.iter().enumerate() {
                    write!(f, "{:?}", (*c).borrow().id())?;
                    if i != children.len() - 1 {
                        write!(f, ", ")?;
                    }
                }
                write!(f, " )")
            },
            N::Node { id, rank, children, .. } => {
                write!(f, "Node id: {} rank: {} ( ", id, rank)?;
                for (i, c) in children.iter().enumerate() {
                    write!(f, "{:?}", (*c).borrow().id())?;
                    if i != children.len() - 1 {
                        write!(f, ", ")?;
                    }
                }
                write!(f, " )")
            },
        }
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

    fn children_mut(&mut self) -> &mut VecDeque<Rc<RefCell<N>>> {
        match self {
            N::Root { children, .. } |
            N::Node { children, .. } => children
        }
    }
}

impl RankedTree {
    pub fn new() -> RankedTree {
        let mut nodes = HashMap::new();
        nodes.insert(0, Rc::new(RefCell::new(N::Root {   
            id: 0,
            children: VecDeque::new(),
        })));
        return RankedTree(nodes, 0);
    }

    pub fn add_node(&mut self, prev: usize, rank: usize) {
        let prev_node = self.node_ref(prev);
        let mut children: VecDeque<Rc<RefCell<N>>> = VecDeque::new();
        let parent = if prev == 0 ||
            (*prev_node).borrow().rank().unwrap() < rank {
            prev_node
        } else {
            (*prev_node).borrow().parent().unwrap().upgrade().unwrap()
        };

        let mut parent_borrowed = (*parent).borrow_mut();
        let siblings = parent_borrowed.children_mut();

        while !siblings.is_empty() &&
              (*siblings.get(0).unwrap()).borrow().rank().unwrap() > rank {
            children.push_back(siblings.pop_front().unwrap());
        }

        let id = self.next_id();
        let node = Rc::new(RefCell::new(N::Node {
            id: id,
            rank: rank,
            parent: Rc::downgrade(&parent),
            children: children,
        }));

        siblings.push_front(Rc::clone(&node));
        self.0.insert(id, node);
    }

    fn next_id(&mut self) -> usize {
        self.1 += 1;
        return self.1;
    }

    fn node_ref(&self, id: usize) -> Rc<RefCell<N>> {
        match self.0.get(&id) {
            Some(node) => Rc::clone(&node),
            None => panic!("Invalid Node id: {}", &id),
        }
    }
}

pub fn yamae_test() {
    let mut tree = RankedTree::new();
    tree.add_node(0, 1);
    tree.add_node(1, 1);
    println!("{:?}", &tree);
    println!("{:?}", &tree.0.get(&0));
}