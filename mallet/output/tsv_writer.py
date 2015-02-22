import gzip, sys, re

# TODO: unit test
def write_stats(stats, out_filename):

    fd = sys.stdout
    if out_filename is not None:
        fd = open(out_filename, 'w')

    stat_names = sorted(stats.keys())
    fd.write("\t".join(["positions"] + stat_names) + "\n")

    positions = sorted(stats[stat_names[0]].keys())
    for position in positions:
        row = [str(position)]
        for stat_name in stat_names:
            row.append("{:.4f}".format(stats[stat_name][position]))
        fd.write("\t".join(row) + "\n")

    fd.close()

def write_emission_frequencies_per_position(frequencies, out_filename):

    fd = sys.stdout
    if out_filename is not None:
        fd = open(out_filename, 'w')

    positions = sorted(frequencies.keys())
    emissions = sorted(frequencies[positions[0]].keys())

    fd.write("\t".join(["pos"] + emissions) + "\n")

    for position, emissions in frequencies.iteritems():
        row = [str(position)]
        for emission, probability in emissions.iteritems():
            row.append("{:.4f}".format(probability))
        fd.write("\t".join(row) + "\n")

    fd.close()


