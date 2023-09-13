pub trait Heap<T>
where
    T: PartialOrd,
{
    fn push(&mut self, v: T);
    fn pop(&mut self) -> Option<T>;
}

pub struct MinHeap<T>(Vec<Option<T>>) where T: PartialOrd;

impl<T: PartialOrd> Heap<T> for MinHeap<T> {
    fn push(&mut self, v: T) {
        let mut idx = self.len();
        self.0.push(Some(v));

        while self.parent(idx) > self.get(idx) {
            let pidx = self.pindex(idx).expect("Check condition.");
            self.0.swap(idx, pidx);
            idx = pidx;
        }
    }

    fn pop(&mut self) -> Option<T> {
        let (v, mut idx) = ({
            let idx = self.len() - 1;
            self.0.swap(1, idx);
            self.0.pop()
        }, 1);

        loop {
            let cidx = match (self.left(idx), self.right(idx)) {
                (Some(l), Some(r)) => {
                    if l <= r {
                        self.lindex(idx)
                    } else {
                        self.rindex(idx)
                    }
                },
                (Some(_), None) => self.lindex(idx),
                (None, Some(c)) => self.rindex(idx),
                (None, None) => None,
            };

            if let Some(c) = cidx {
                if self.get(c) < self.get(idx) {
                    self.0.swap(idx, c);
                    idx = c;
                } else {
                    break;
                }
            } else { break; }
        }

        v?
    }
}

impl<T: PartialOrd> MinHeap<T> {
    pub fn new() -> MinHeap<T> {
        MinHeap::<T>(vec![None])
    }

    fn len(&self) -> usize {
        self.0.len()
    }

    fn get(&self, index: usize) -> Option<&T> {
        if index > 0 && index < self.len() {
            self.0[index].as_ref()
        } else { None }
    }

    fn parent(&self, index: usize) -> Option<&T> {
        self.0[self.pindex(index)?].as_ref()
    }

    fn left(&self, index: usize) -> Option<&T> {
        self.0[self.lindex(index)?].as_ref()
    }

    fn right(&self, index: usize) -> Option<&T> {
        self.0[self.rindex(index)?].as_ref()
    }
    
    fn pindex(&self, index: usize) -> Option<usize> {
        Some(index / 2).filter(|i| i > &0)
    }

    fn lindex(&self, index: usize) -> Option<usize> {
        Some(index * 2).filter(|i| i < &self.len())
    }

    fn rindex(&self, index: usize) -> Option<usize> {
        Some(index * 2 + 1).filter(|i| i < &self.len())
    }
}

#[cfg(test)]
mod test {
    use crate::heap::{Heap, MinHeap};

    #[test]
    fn test_push_ascending() {
        let mut h = MinHeap::new();
        h.push(1);
        h.push(2);
        assert_eq!(h.0, vec![None, Some(1), Some(2)]);
    }

    #[test]
    fn test_push_descending() {
        let mut h = MinHeap::new();
        h.push(3);
        h.push(2);
        h.push(1);
        assert_eq!(h.0, vec![None, Some(1), Some(3), Some(2)]);
    }

    #[test]
    fn test_push_random() {
        let mut h = MinHeap::new();
        h.push(5);
        h.push(2);
        h.push(1);
        h.push(4);
        h.push(3);
        let expected = [None, Some(1), Some(3), Some(2), Some(5), Some(4)];
        assert_eq!(h.0, expected);
    }

    #[test]
    fn test_pop() {
        let mut h = MinHeap::new();
        h.push(5);
        h.push(2);
        h.push(1);
        h.push(4);
        h.push(3);
        assert_eq!(Some(1), h.pop());
        println!("{:?}", h.0);
        assert_eq!(Some(2), h.pop());
        assert_eq!(Some(3), h.pop());
        assert_eq!(Some(4), h.pop());
        assert_eq!(Some(5), h.pop());
    }
}
