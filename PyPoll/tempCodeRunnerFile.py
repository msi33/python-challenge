 find the winner
# winning_candidate = ""
# winning_candidate_votes = 0
# for candidate in candidates:
#     current_votes = candidate_votes[candidates.index(candidate)]
#     if current_votes > winning_candidate_votes:
#         winning_candidate = candidate
#         winning_candidate_votes = current_votes

# # print the results to screen
# print('Election Results')
# print('-------------------------')
# print(f'Total Votes: {total_votes}')
# print('-------------------------')
# for candidate in candidates:
#     current_candidate_votes = candidate_votes[candidates.index(candidate)]
#     current_vote_pct = (current_candidate_votes / total_votes) * 100
#     print(
#         f'{candidate}: {round(current_vote_pct,3)}% ({current_candidate_votes})')
# print('-------------------------')
# print(f'Winner: {winning_candidate}')
# print('-------------------------')

# # print the results to file
# out_file_path = "PyPoll\election_results.txt"
# with open(out_file_path, 'w') as file_out:
#     file_out.write('Election Results\n')
#     file_out.write('-------------------------\n')
#     file_out.write(f'Total Votes: {total_votes}\n')
#     file_out.write('-------------------------\n')
#     for candidate in candidates:
#         current_candidate_votes = candidate_votes[candidates.index(candidate)]
#         current_vote_pct = (current_candidate_votes / total_votes) * 100
#         file_out.write(
#             f'{candidate}: {round(current_vote_pct,3)}% ({current_candidate_votes})\n')
#     file_out.write('-------------------------\n')
#     file_out.write(f'Winner: {winning_candidate}\n')
#     file_out.write('-------------------------\n')
# # end here
