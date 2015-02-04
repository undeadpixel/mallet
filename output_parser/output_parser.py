def output_generator(output_filename, seq, score, log_score, struct ):

    output = open(output_filename, 'w')
    output.write(("%s\nScore:%s\tLog_Score:%s\n%s\n\n" % (seq, score, log_score, struct)))
    output.close()
