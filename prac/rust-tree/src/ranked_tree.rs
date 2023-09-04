use std::cell::RefCell;
use std::collections::{ HashMap, VecDeque };
use std::fmt;
use std::rc::{ Rc, Weak };

#[derive(Debug)]
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

impl fmt::Debug for RankedNode {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            N::Root { id, children } => {
                f.debug_struct("RankedNode::Root")
                 .field("id", id)
                 .field("children", &(children.iter().fold(String::from("[ "), |acc, c| {
                    acc + &(*c).borrow().id().to_string() + " "
                 }) + "]"))
                 .finish()
            },
            N::Node { id, rank, parent, children } => {
                f.debug_struct("RankedNode::Node")
                 .field("id", id)
                 .field("rank", rank)
                 .field("parent", &parent.upgrade().unwrap().borrow().id().to_string())
                 .field("children", &(children.iter().fold(String::from("[ "), |acc, c| {
                    acc + &(*c).borrow().id().to_string() + " "
                 }) + "]"))
                 .finish()
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
    
    fn id_from_reference(reference: &Rc<RefCell<N>>) -> usize {
        (*reference).borrow().id()
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

    fn set_parent(&mut self, n: Rc<RefCell<N>>) -> Result<(), String> {
        match self {
            N::Root { .. } => Err(String::from("Root Node.")),
            N::Node { parent, .. } => Ok(*parent = Rc::downgrade(&n)),
        }
    }

    fn children(&self) -> &VecDeque<Rc<RefCell<N>>> {
        match self {
            N::Root { children, .. } |
            N::Node { children, .. } => children
        }
    }

    fn children_mut(&mut self) -> &mut VecDeque<Rc<RefCell<N>>> {
        match self {
            N::Root { children, .. } |
            N::Node { children, .. } => children
        }
    }

    fn child(&self, index: usize) -> Option<Rc<RefCell<N>>> {
        self.children().get(index).map(|c| Rc::clone(c))
    }

    fn child_index_by_id(&self, child_id: usize) -> Option<usize> {
        self.children().iter().position(|c| (*c).borrow().id() == child_id)
    }

    fn prev(&self) -> Option<Rc<RefCell<N>>> {
        if let Some(parent) = self.parent().and_then(|p| p.upgrade()) {
            match (*parent).borrow().child_index_by_id(self.id()).unwrap() {
                0 => Some(Rc::clone(&parent)),
                i => (*parent).borrow().child(i - 1),
            }
        } else {
            None
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

    pub fn add_node(&mut self, rank: usize, prev: usize) {
        let mut prev_node = self.node_ref(prev);
        let mut children: VecDeque<Rc<RefCell<N>>> = VecDeque::new();
        let mut parent = if prev == 0 || (*prev_node).borrow().rank().unwrap() < rank {
            prev_node
        } else {
            (*prev_node).borrow().parent().unwrap().upgrade().unwrap()
        };

        let mut parent_borrowed = (*parent).borrow_mut();
        let mut siblings = parent_borrowed.children_mut();

        while !siblings.is_empty() && (*siblings.get(0).unwrap()).borrow().rank().unwrap() > rank {
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
    tree.add_node(1, 0);
    tree.add_node(2, 1);
    println!("{:?}", &tree);
}