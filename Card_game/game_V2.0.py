import random
from collections import Counter

def create_deck():
    """ქმნის 4 დასტას (208 კარტი სულ)"""
    try:
        suits = ['S', 'H', 'D', 'C']  # Spade, Heart, Diamond, Club
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        deck = []
        
        # ვქმნით 4 დასტას
        for deck_num in range(4):
            for suit in suits:
                for value in values:
                    deck.append(f"{value}{suit}")
        
        if len(deck) != 208:
            raise ValueError(f"დასტაში უნდა იყოს 208 კარტი (4 დასტა), მაგრამ შეიქმნა {len(deck)}")
        return deck
    except Exception as e:
        print(f"შეცდომა დასტის შექმნისას: {e}")
        raise

def shuffle_and_deal(deck, num_players, cards_per_player):
    """აურევს დასტას და გაანაწილებს კარტებს მოთამაშეებს"""
    try:
        if not deck:
            raise ValueError("დასტა ცარიელია")
        if num_players <= 0:
            raise ValueError("მოთამაშეების რაოდენობა უნდა იყოს 0-ზე მეტი")
        if cards_per_player <= 0:
            raise ValueError("კარტების რაოდენობა თითო მოთამაშეზე უნდა იყოს 0-ზე მეტი")
        if len(deck) < num_players * cards_per_player:
            raise ValueError(f"არასაკმარისი კარტები: საჭიროა {num_players * cards_per_player}, არის {len(deck)}")
        
        shuffled_deck = deck.copy()
        random.shuffle(shuffled_deck)
        
        players_cards = []
        for i in range(num_players):
            start_idx = i * cards_per_player
            end_idx = start_idx + cards_per_player
            players_cards.append(shuffled_deck[start_idx:end_idx])
        
        return players_cards
    except Exception as e:
        print(f"შეცდომა კარტების განაწილებისას: {e}")
        raise

def calculate_score(cards):
    """ითვლის მოთამაშის ქულებს"""
    try:
        if not cards:
            raise ValueError("კარტების სია ცარიელია")
        
        score = 0
        for card in cards:
            if not card or len(card) < 2:
                raise ValueError(f"არასწორი კარტის ფორმატი: {card}")
            
            value = card[:-1]  # ამოვიღოთ მნიშვნელობა (ბოლო სიმბოლო არის ფერი)
            
            if value == 'A':
                score += 20
            elif value == 'J':
                score += 11
            elif value == 'Q':
                score += 12
            elif value == 'K':
                score += 13
            else:
                try:
                    score += int(value)
                except ValueError:
                    raise ValueError(f"არასწორი კარტის მნიშვნელობა: {value}")
        
        return score
    except Exception as e:
        print(f"შეცდომა ქულების გამოთვლისას: {e}")
        raise

def get_card_values(cards):
    """აბრუნებს კარტების მნიშვნელობებს (A, J, Q, K, 2-10)"""
    try:
        if not cards:
            raise ValueError("კარტების სია ცარიელია")
        
        values = []
        for card in cards:
            if not card or len(card) < 2:
                raise ValueError(f"არასწორი კარტის ფორმატი: {card}")
            value = card[:-1]  # ამოვიღოთ მნიშვნელობა
            values.append(value)
        return values
    except Exception as e:
        print(f"შეცდომა კარტების მნიშვნელობების მიღებისას: {e}")
        raise

def find_winner_by_duplicates(scores, players_cards, active_players):
    """თანაბარი ქულების შემთხვევაში ამოწმებს მეტი ერთიდაიმავე მნიშვნელობის კარტებს"""
    try:
        if not active_players:
            raise ValueError("აქტიური მოთამაშეები არ არის")
        
        active_scores = [scores[i] for i in active_players]
        if not active_scores:
            raise ValueError("ქულების სია ცარიელია")
        
        max_score = max(active_scores)
        tied_players = [i for i in active_players if scores[i] == max_score]
        
        if len(tied_players) <= 1:
            return tied_players[0] if tied_players else None
        
        # თითოეული მოთამაშისთვის ვიპოვოთ ყველაზე მეტი ერთიდაიმავე მნიშვნელობის კარტების რაოდენობა
        player_duplicates = []
        for player_idx in tied_players:
            if player_idx >= len(players_cards):
                raise IndexError(f"მოთამაშის ინდექსი {player_idx} არასწორია")
            card_values = get_card_values(players_cards[player_idx])
            value_counts = Counter(card_values)
            if not value_counts:
                raise ValueError(f"მოთამაშე {player_idx}-ს არ აქვს კარტები")
            max_count = max(value_counts.values())
            player_duplicates.append((player_idx, max_count, value_counts))
        
        if not player_duplicates:
            return None
        
        # ვიპოვოთ მაქსიმალური დუბლიკატების რაოდენობა
        max_duplicates = max([dup_count for _, dup_count, _ in player_duplicates])
        players_with_max_duplicates = [(idx, dup_count, counts) for idx, dup_count, counts in player_duplicates 
                                       if dup_count == max_duplicates]
        
        if len(players_with_max_duplicates) == 1:
            return players_with_max_duplicates[0][0]
        
        # თუ რამდენიმე მოთამაშეს აქვს ერთიდაიმავე რაოდენობის დუბლიკატები, ვამოწმებთ მნიშვნელობებს
        value_order = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
                      'J': 11, 'Q': 12, 'K': 13, 'A': 20}
        
        max_value_score = -1
        winner = None
        
        for player_idx, dup_count, value_counts in players_with_max_duplicates:
            # ვიპოვოთ მაქსიმალური მნიშვნელობა, რომელსაც აქვს max_duplicates რაოდენობა
            matching_values = [v for v, c in value_counts.items() if c == max_duplicates]
            if not matching_values:
                continue
            max_value = max(matching_values, key=lambda x: value_order.get(x, 0))
            value_score = value_order.get(max_value, 0)
            
            if value_score > max_value_score:
                max_value_score = value_score
                winner = player_idx
            elif value_score == max_value_score:
                # თუ ისევ თანაბარია, ფრეა
                winner = None
        
        return winner
    except Exception as e:
        print(f"შეცდომა გამარჯვებულის პოვნისას: {e}")
        return None

def display_cards(players, players_cards, active_players):
    """აჩვენებს მოთამაშეების კარტებს"""
    try:
        if not active_players:
            print("აქტიური მოთამაშეები არ არის")
            return
        
        print("\n" + "="*60)
        for i in active_players:
            if i >= len(players):
                print(f"შეცდომა: მოთამაშის ინდექსი {i} არასწორია")
                continue
            if i >= len(players_cards):
                print(f"შეცდომა: მოთამაშე {players[i]}-ს არ აქვს კარტები")
                continue
            try:
                cards_str = ", ".join(players_cards[i])
                score = calculate_score(players_cards[i])
                print(f"{players[i]}: {cards_str} | ქულები: {score}")
            except Exception as e:
                print(f"შეცდომა მოთამაშე {players[i]}-ის კარტების ჩვენებისას: {e}")
        print("="*60)
    except Exception as e:
        print(f"შეცდომა კარტების ჩვენებისას: {e}")

def find_loser(scores, players_cards, active_players, winner):
    """ვიპოვოთ დამარცხებული მოთამაშე"""
    losers = None
    try:
        if winner is None:
            raise ValueError("გამარჯვებული არ არის განსაზღვრული")
        if winner not in active_players:
            raise ValueError(f"გამარჯვებული {winner} არ არის აქტიურ მოთამაშეებში")
        
        losers = [i for i in active_players if i != winner]
        
        if not losers:
            raise ValueError("დამარცხებული მოთამაშეები არ არის")
        
        if len(losers) == 1:
            return losers[0]
        
        # ვიპოვოთ ყველაზე დაბალი ქულა
        loser_scores = []
        for i in losers:
            if i >= len(scores):
                raise IndexError(f"მოთამაშის ინდექსი {i} არასწორია ქულების სიაში")
            loser_scores.append((i, scores[i]))
        
        loser_scores.sort(key=lambda x: x[1])
        lowest_score = loser_scores[0][1]
        losers_with_lowest = [i for i, score in loser_scores if score == lowest_score]
        
        if len(losers_with_lowest) == 1:
            return losers_with_lowest[0]
        
        # თუ რამდენიმე დამარცხებულს აქვს თანაბარი ქულა, ვამოწმებთ დუბლიკატებს
        # ის, ვისაც ნაკლები ერთიდაიმავე მნიშვნელობის კარტი აქვს, ტოვებს
        min_duplicates = float('inf')
        loser = None
        
        for player_idx in losers_with_lowest:
            if player_idx >= len(players_cards):
                raise IndexError(f"მოთამაშის ინდექსი {player_idx} არასწორია კარტების სიაში")
            card_values = get_card_values(players_cards[player_idx])
            value_counts = Counter(card_values)
            if not value_counts:
                continue
            max_count = max(value_counts.values())
            
            if max_count < min_duplicates:
                min_duplicates = max_count
                loser = player_idx
            elif max_count == min_duplicates and loser is not None:
                # თუ ისევ თანაბარია, ვირჩევთ პირველს
                pass
        
        return loser if loser is not None else losers_with_lowest[0]
    except Exception as e:
        print(f"შეცდომა დამარცხებულის პოვნისას: {e}")
        # თუ შეცდომა მოხდა, ვირჩევთ პირველ დამარცხებულს
        if losers and len(losers) > 0:
            return losers[0]
        # თუ losers არ არის განსაზღვრული, ვცდილობთ ვიპოვოთ ნებისმიერი დამარცხებული
        try:
            if active_players and winner is not None and winner in active_players:
                remaining = [i for i in active_players if i != winner]
                if remaining:
                    return remaining[0]
        except:
            pass
        raise

def play_round(players, deck, active_players):
    """ითამაშებს ერთ რაუნდს"""
    try:
        if not active_players:
            raise ValueError("აქტიური მოთამაშეები არ არის")
        if not deck:
            raise ValueError("დასტა ცარიელია")
        
        cards_per_player = 5
        players_cards = shuffle_and_deal(deck, len(players), cards_per_player)
        
        # გამოვთვალოთ ქულები
        scores = []
        for i in range(len(players)):
            if i in active_players:
                try:
                    score = calculate_score(players_cards[i])
                    scores.append(score)
                except Exception as e:
                    print(f"შეცდომა მოთამაშე {players[i]}-ის ქულების გამოთვლისას: {e}")
                    scores.append(0)
            else:
                scores.append(0)
        
        # ვაჩვენოთ კარტები
        display_cards(players, players_cards, active_players)
        
        # ვიპოვოთ გამარჯვებული
        active_scores = [scores[i] for i in active_players]
        if not active_scores:
            raise ValueError("აქტიური მოთამაშეების ქულები არ არის")
        
        max_score = max(active_scores)
        winners = [i for i in active_players if scores[i] == max_score]
        
        if len(winners) == 1:
            # ერთი გამარჯვებული - ვიპოვოთ დამარცხებული
            winner = winners[0]
            try:
                loser = find_loser(scores, players_cards, active_players, winner)
                return winner, loser
            except Exception as e:
                print(f"შეცდომა დამარცხებულის პოვნისას: {e}")
                return winner, None
        else:
            # თანაბარი ქულები - ვამოწმებთ დუბლიკატებს
            winner = find_winner_by_duplicates(scores, players_cards, active_players)
            
            if winner is not None:
                # გამარჯვებული გამოვლინდა - ვიპოვოთ დამარცხებული
                try:
                    loser = find_loser(scores, players_cards, active_players, winner)
                    return winner, loser
                except Exception as e:
                    print(f"შეცდომა დამარცხებულის პოვნისას: {e}")
                    return winner, None
            else:
                # ფრე - არავინ ტოვებს
                return None, None
    except Exception as e:
        print(f"შეცდომა რაუნდის თამაშისას: {e}")
        return None, None

def main():
    """მთავარი თამაშის ფუნქცია"""
    try:
        print("კარტების თამაში - 3 მოთამაშე")
        print("="*60)
        
        # მოთამაშეების სახელების შეყვანა
        players = []
        for i in range(3):
            try:
                name = input(f"შეიყვანეთ {i+1}-ლი მოთამაშის სახელი: ").strip()
                if not name:
                    raise ValueError("სახელი არ შეიძლება იყოს ცარიელი")
                players.append(name)
            except KeyboardInterrupt:
                print("\n\nთამაში შეწყდა მომხმარებლის მიერ")
                return
            except Exception as e:
                print(f"შეცდომა სახელის შეყვანისას: {e}")
                players.append(f"მოთამაშე {i+1}")
        
        if len(players) != 3:
            raise ValueError("უნდა იყოს ზუსტად 3 მოთამაშე")
        
        active_players = set(range(3))  # აქტიური მოთამაშეების ინდექსები
        
        try:
            deck = create_deck()
        except Exception as e:
            print(f"შეცდომა დასტის შექმნისას: {e}")
            return
        
        round_num = 1
        max_rounds = 100  # მაქსიმალური რაუნდების რაოდენობა, რათა არ მოხდეს უსასრულო ციკლი
        
        while len(active_players) > 1 and round_num <= max_rounds:
            try:
                print(f"\n{'='*60}")
                print(f"რაუნდი {round_num}")
                print(f"{'='*60}")
                
                winner, loser = play_round(players, deck, active_players)
                
                if winner is not None and loser is not None:
                    if winner >= len(players) or loser >= len(players):
                        print("შეცდომა: მოთამაშის ინდექსი არასწორია")
                        break
                    print(f"\nგამარჯვებული: {players[winner]}")
                    print(f"დამარცხებული და გამორიცხული: {players[loser]}")
                    active_players.remove(loser)
                elif winner is not None:
                    if winner >= len(players):
                        print("შეცდომა: მოთამაშის ინდექსი არასწორია")
                        break
                    print(f"\nგამარჯვებული: {players[winner]}")
                    print("ფრე - არავინ ტოვებს თამაშს")
                else:
                    print("\nფრე - არავინ ტოვებს თამაშს")
                
                round_num += 1
            except KeyboardInterrupt:
                print("\n\nთამაში შეწყდა მომხმარებლის მიერ")
                return
            except Exception as e:
                print(f"შეცდომა რაუნდის დროს: {e}")
                round_num += 1
                continue
        
        if round_num > max_rounds:
            print(f"\nმიღწეულია მაქსიმალური რაუნდების რაოდენობა ({max_rounds})")
        
        # ბოლო გამარჯვებული
        if len(active_players) == 1:
            winner_idx = list(active_players)[0]
            if winner_idx < len(players):
                print(f"\n{'='*60}")
                print(f"🎉 საბოლოო გამარჯვებული: {players[winner_idx]}! 🎉")
                print(f"{'='*60}")
            else:
                print("შეცდომა: გამარჯვებულის ინდექსი არასწორია")
        elif len(active_players) == 0:
            print("\nყველა მოთამაშე დატოვა თამაში")
        else:
            print(f"\nთამაში დასრულდა. დარჩენილი მოთამაშეები: {len(active_players)}")
    
    except KeyboardInterrupt:
        print("\n\nთამაში შეწყდა მომხმარებლის მიერ")
    except Exception as e:
        print(f"\nკრიტიკული შეცდომა: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()

