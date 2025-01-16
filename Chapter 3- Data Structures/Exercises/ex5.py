## Exercise 5: Change Guest List :ballot_box_with_check:

# You just heard that one of your guests can’t make the
# dinner, so you need to send out a new set of invitations. You’ll have to think of
# someone else to invite.

# •Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.

# •Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.

# •Print a second set of invitation messages, one for each person who is still in your list.
guests = ["Albert Einstein", "Leonardo da Vinci", "Elon Musk"]

print(guests[1] + " can't make it to the dinner.")

guests[1] = "Benjamin Franklin"

print("Updated Invitations:")
print("Dear " + guests[0] + ", I would be thrilled to discuss the mysteries of the universe with you over dinner.")
print("Dear " + guests[1] + ", it would be fascinating to talk about your pioneering work in science.")
print("Dear " + guests[2] + ", I would love to talk about the future of technology and space exploration with you.")

