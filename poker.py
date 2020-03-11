from collections import Counter

def sort_cards_values(hand):
	"""
	Return a list of the cards values sorted with higher first.
	"""
	cards = []
	for value in hand:
		if value[0] == 'A':
			value = 14
		elif value[0] == 'K':
			value = 13
		elif value[0] == 'Q':
			value = 12
		elif value[0] == 'J':
			value = 11
		elif value[0] == 'T':
			value = 10
		else:
			value = int(value[0])
		cards.append(value)
	sortedHand=sorted(cards,reverse=True)
	return sortedHand

def is_royal_flush(values, hand):
	"""
	Return True if the card values are [14, 13, 12, 11, 10] and all are the same suit.
	This conditions happens when hand is straight and flush.
	"""
	return is_straight(values) and is_flush(hand) and values == [14, 13, 12, 11, 10]

def is_straight(values):
	"""
	Return True if the ordered cards are in sequence, all in the same suit.
	"""
	for i in range(1, len(values)):
		if values[i] == values[i - 1] - 1:
			return True
		else:
			return False

def is_flush(hand):
	"""
	Return True if the five cards have the same suit, but not in a sequence
	"""
	return len(set(suit for rank, suit in hand)) == 1

def is_n_kind(n, values):
	"""
	Return the value of the n cards with the same rank and otherwise return None
	"""
	count_val = Counter(values)
	sorted_count = sorted(count_val.items(), reverse=True)
	for num, rep in sorted_count:
		if rep == n:
			return num
		else:
			return 0
	
def is_two_pair(values):
	"""
	Using the is_n_kind function validate if there are a two pair. If so, return the highest and lowest.
	"""
	pair_highest = is_n_kind(2, values)
	pair_lowest = is_n_kind(2, list(reversed(values)))
	if pair_highest != pair_lowest and pair_highest and pair_lowest:
		return pair_highest, pair_lowest
	else:
		return 0

class Result():
	WIN = 1
	LOSS = 0

class PokerHand:
	def __init__(self, hand):
		self.hand = hand.split()
		self.rank = self.hand_rank()

	def hand_rank(self):
		"""
		Return an array with 2 values indicating the rank of a hand
		and the sorted hand. 
		"""
		values_sorted = sort_cards_values(self.hand)
		if is_royal_flush(values_sorted, self.hand):
			return [9, values_sorted]
		elif is_straight(values_sorted) and is_flush(self.hand):
			return [8, max(values_sorted)]
		elif is_n_kind(4, values_sorted):
			return [7, is_n_kind(4, values_sorted), is_n_kind(1, values_sorted)]
		elif is_n_kind(3, values_sorted) and is_n_kind(2, values_sorted):
			return [6, is_n_kind(3, values_sorted), is_n_kind(2, values_sorted)]
		elif is_flush(self.hand):
			return [5, values_sorted]
		elif is_straight(values_sorted):
			return [4, max(values_sorted)]
		elif is_n_kind(3, values_sorted):
			return [3, is_n_kind(3, values_sorted), values_sorted]
		elif is_two_pair(values_sorted):
			return [2, is_two_pair(values_sorted), values_sorted]
		elif is_n_kind(2, values_sorted):
			return [1, is_n_kind(2, values_sorted), values_sorted]
		else:
			return [0, values_sorted]

	def compare_with(self, new_hand):
		"""
		Return Result.WIN if the current poker hand ranking is higher 
		than a new poker hand else return Result.LOSS.
		"""
		if self.rank[0] > new_hand.rank[0]:
			result = Result.LOSS
		elif self.rank[0] < new_hand.rank[0]:
			result = Result.WIN
		elif self.rank[0] == new_hand.rank[0]:
			if self.rank[1] > new_hand.rank[1]:
				result = Result.LOSS
			else:
				result = Result.WIN
		return result